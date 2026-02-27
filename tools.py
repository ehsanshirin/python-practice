# math_tools.py

# متغیر سطح ماژول
PI = 3.14159

def add(a, b):
    """جمع دو عدد"""
    return a + b


def multiply(a, b):
    """ضرب دو عدد"""
    return a * b


def circle_area(radius):
    """مساحت دایره"""
    return PI * radius ** 2


# این قسمت فقط وقتی فایل مستقیم اجرا شود اجرا می‌شود (نه وقتی import شود)
if __name__ == "__main__":
    print("این فایل به صورت مستقیم اجرا شد!")
    print("تست تابع:", add(10, 25))