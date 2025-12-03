class Laptop:
    def __init__(self,brand):
        self.brand = brand
        self.ram = 8
        self.cpu = 'i3'

    def set_spece(self,ram,cpu):
        if ram < 4:
            print('AM cannot be less than 4GB')
            return
        
        self.ram = ram
        self.cpu = cpu
        print(f'{self.brand} spece updated: RAM = {self.ram}, CPU = {self.cpu}')
        

    def show_spece(self):
        print(f'Laptop {self.brand} ram is {self.ram} & cpu is {self.cpu}')
        


laptop1 = Laptop('HP')
laptop2 = Laptop('Dell')

laptop1.set_spece(16,'i7')
laptop2.set_spece(8,'i5')


laptop1.show_spece()
laptop2.show_spece()