class TV:
    def __init__(self, brand):
        self.brand = brand
        self.volume = 10
        self.is_on = 'OFF'
    
    def turn_on(self):
        if self.is_on == 'ON':
            print(f'{self.brand} is ON. Now')
        self.is_on = 'ON'
        print(f'{self.brand} is ON')
        
        
    def turn_off(self):
        if self.is_on == 'OFF':
            print(f'{self.brand} is OFF. Now')
        self.is_on = 'OFF'
        print(f'{self.brand} is OFF')
        
    def volume_up(self, amount):
        if amount <= 0:
            print('Error')
            return
        
        self.volume += amount
        if self.volume > 100:
            self.volume = 100
            
        print(f'Volume is {self.volume}, Now')    
        
        
    def volume_down(self, amount):
        if amount <= 0:
            print('Error')
            return
        self.volume -= amount
        if self.volume < 0:
            self.volume = 0
        
        print(f'Volume is {self.volume}, Now')
    
            
    def info (self):
        print(f'{self.brand} is Now {self.is_on} and Volume is {self.volume}')
        

class Remote:
    def __init__(self, tv):
        self.tv = tv
        
    def power_on(self):
        self.tv.turn_on()
        
    def power_off(self):
        self.tv.turn_off()
        
    def volume_up(self, amount):
        self.tv.volume_up(amount)
        
    def volume_down(self, amount):
        self.tv.volume_down(amount)
        
    def show_status(self):
        self.tv.info()
        
        
        
        
tv1 = TV('LG')
rmt1 = Remote(tv1)

rmt1.power_on()
rmt1.volume_up(20)
rmt1.volume_down(4)
rmt1.show_status()