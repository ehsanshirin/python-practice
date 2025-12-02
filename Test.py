<<<<<<< HEAD
def test (a , b ,c):
    return max (a, b, c)
print(test(10,3,6))
=======
class Laptop:
    def __init__(self,brand):
        self.brand = brand
    
    def set_specs(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu


pc_1 = Laptop('HP')
pc_1.set_specs('ram is 8', 'cpu is core i 5')
print(pc_1.brand, pc_1.ram, pc_1.cpu)
>>>>>>> cbdf8685009cd95be77828d0990f350ab6503698
