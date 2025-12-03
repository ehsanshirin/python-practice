class Phone:
    def __init__(self,brand):
        self.brand = brand
        self.memory = 64
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f'{self.brand} is on')

    def turn_off(self):
        self.is_on = False
        print(f'{self.brand} is off')

    def add_memory(self,extra):
        if extra <= 0:
            print('ram is not enough')
            return
        self.memory += extra
        print(f'New Memory is: {self.memory}gig')


phone1 = Phone('Apple')
phone2 = Phone('Xiaomi')

phone1.turn_on()
phone1.add_memory(50)

phone2.turn_off()
phone2.add_memory(20)
