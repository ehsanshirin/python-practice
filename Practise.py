class Shop:
    def __init__(self, brand, memory):
        self.brnad = brand
        self.memory = memory
        self.is_on = 'off'

    def add_memory(self, extra):
        if extra <= 0:
            print('Error')
            return
        self.memory += extra
        print(f'{self.brnad}: New Memory: {self.memory}GB')

    def info(self):
        print(f'{self.brnad}: Memory is {self.memory} and Now is {self.is_on}')

    def turn_on(self):
        self.is_on = 'ON'
        print(f'{self.brnad} is ON')

    def turn_off(self):
        self.is_on = 'OFF'
        print(f'{self.brnad} is OFF')


phone1 = Shop('Samsung', 64)
phone1.turn_on()
phone1.info()
