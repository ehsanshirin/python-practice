import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec

# Settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 900
MAX_POINTS = 500
VISIBLE_POINTS = 50
UPDATE_INTERVAL = 500  # ms

# Thresholds
TEMP_MAX = 28.0
HUM_MAX = 70.0
SOIL_MIN = 30.0
LIGHT_MIN = 400.0

# Actuator states
fan_state = False
led_state = False
pump_state = False

# Data queues
time_data = deque(maxlen=MAX_POINTS)
temp_data = deque(maxlen=MAX_POINTS)
hum_data = deque(maxlen=MAX_POINTS)
soil_data = deque(maxlen=MAX_POINTS)
light_data = deque(maxlen=MAX_POINTS)

# Sensor simulation
def read_temperature():
    return random.uniform(18, 30)
def read_humidity():
    return random.uniform(40, 80)
def read_soil_moisture():
    return random.uniform(20, 70)
def read_light():
    return random.uniform(200, 800)

# Manual control
def toggle_fan():
    global fan_state
    fan_state = not fan_state
def toggle_led():
    global led_state
    led_state = not led_state
def toggle_pump():
    global pump_state
    pump_state = not pump_state

# Tkinter UI
root = tk.Tk()
root.title("Smart Greenhouse Dashboard")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Time interval options
time_intervals = {
    "Minute": timedelta(minutes=1),
    "Hourly": timedelta(hours=1),
    "Daily": timedelta(days=1),
    "Weekly": timedelta(weeks=1),
    "Monthly": timedelta(days=30)
}
selected_interval = tk.StringVar(value="Minute")

# Left frame for charts
frame_chart = tk.Frame(root)
frame_chart.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Matplotlib figure with 2x2 layout
fig = plt.Figure(figsize=(10,8))
gs = GridSpec(2,2, figure=fig)
axs = [fig.add_subplot(gs[0,0]),
       fig.add_subplot(gs[0,1]),
       fig.add_subplot(gs[1,0]),
       fig.add_subplot(gs[1,1])]

canvas = FigureCanvasTkAgg(fig, master=frame_chart)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Navigation toolbar
toolbar = NavigationToolbar2Tk(canvas, frame_chart)
toolbar.update()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Right frame for controls
frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Labels
temp_label = ttk.Label(frame_controls, text="Temperature:")
temp_label.pack(pady=5)
hum_label = ttk.Label(frame_controls, text="Humidity:")
hum_label.pack(pady=5)
soil_label = ttk.Label(frame_controls, text="Soil Moisture:")
soil_label.pack(pady=5)
light_label = ttk.Label(frame_controls, text="Light:")
light_label.pack(pady=5)
fan_label = ttk.Label(frame_controls, text="Fan:")
fan_label.pack(pady=5)
led_label = ttk.Label(frame_controls, text="LED:")
led_label.pack(pady=5)
pump_label = ttk.Label(frame_controls, text="Water Pump:")
pump_label.pack(pady=5)

# Buttons
ttk.Button(frame_controls, text="Toggle Fan", command=toggle_fan).pack(pady=5)
ttk.Button(frame_controls, text="Toggle LED", command=toggle_led).pack(pady=5)
ttk.Button(frame_controls, text="Toggle Pump", command=toggle_pump).pack(pady=5)

# Time interval filter
ttk.Label(frame_controls, text="Time Interval:").pack(pady=5)
ttk.OptionMenu(frame_controls, selected_interval, *time_intervals.keys()).pack(pady=5)

# Lines for animation
lines = [axs[i].plot([], [])[0] for i in range(4)]
titles = ["Temperature","Humidity","Soil Moisture","Light"]
ylabels = ["°C","%","%","lux"]
full_screen = False
full_ax_idx = None

def on_double_click(event):
    global full_screen, full_ax_idx
    if event.dblclick:
        for i, ax in enumerate(axs):
            if ax == event.inaxes:
                if not full_screen:
                    # Hide all other axes
                    for j, a in enumerate(axs):
                        if j != i:
                            a.set_visible(False)
                    full_ax_idx = i
                    full_screen = True
                else:
                    # Restore all axes
                    for a in axs:
                        a.set_visible(True)
                    full_screen = False
                    full_ax_idx = None
                canvas.draw()
                break

canvas.mpl_connect('button_press_event', on_double_click)

def update_chart():
    interval = selected_interval.get()
    delta = time_intervals[interval]
    cutoff = datetime.now() - delta

    times_filtered = [t for t in time_data if t >= cutoff]
    temp_filtered = [temp_data[i] for i, t in enumerate(time_data) if t >= cutoff]
    hum_filtered = [hum_data[i] for i, t in enumerate(time_data) if t >= cutoff]
    soil_filtered = [soil_data[i] for i, t in enumerate(time_data) if t >= cutoff]
    light_filtered = [light_data[i] for i, t in enumerate(time_data) if t >= cutoff]

    data_list = [temp_filtered, hum_filtered, soil_filtered, light_filtered]

    for i, line in enumerate(lines):
        if full_screen and full_ax_idx != i:
            continue
        line.set_data(times_filtered, data_list[i])
        axs[i].relim()
        axs[i].autoscale_view()
        axs[i].grid(True, linestyle='--', alpha=0.6)
        axs[i].set_title(titles[i])
        axs[i].set_ylabel(ylabels[i])
        if i==3 or full_screen:  # format x-axis
            if times_filtered:
                start_idx = max(0, len(times_filtered)-VISIBLE_POINTS)
                axs[i].set_xlim(times_filtered[start_idx], times_filtered[-1])
                axs[i].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
                fig.autofmt_xdate()
    canvas.draw_idle()

def update_data():
    global fan_state, led_state, pump_state
    temperature = read_temperature()
    humidity = read_humidity()
    soil = read_soil_moisture()
    light = read_light()

    fan_state = temperature > TEMP_MAX or humidity > HUM_MAX
    led_state = light < LIGHT_MIN
    pump_state = soil < SOIL_MIN

    now = datetime.now()
    temp_data.append(temperature)
    hum_data.append(humidity)
    soil_data.append(soil)
    light_data.append(light)
    time_data.append(now)

    temp_label.config(text=f"Temperature: {temperature:.1f} °C")
    hum_label.config(text=f"Humidity: {humidity:.1f} %")
    soil_label.config(text=f"Soil Moisture: {soil:.1f} %")
    light_label.config(text=f"Light: {light:.1f} lux")
    fan_label.config(text=f"Fan: {'ON' if fan_state else 'OFF'}")
    led_label.config(text=f"LED: {'ON' if led_state else 'OFF'}")
    pump_label.config(text=f"Water Pump: {'ON' if pump_state else 'OFF'}")

    update_chart()
    root.after(UPDATE_INTERVAL, update_data)

root.after(UPDATE_INTERVAL, update_data)
root.mainloop()
