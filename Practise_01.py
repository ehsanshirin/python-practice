<<<<<<< HEAD
class Car:
    def __init__(self, brand, model, year, color = 'Black'):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def attribute(self):
        print(f'''
              \rBrand: {self.brand}
              \rModel: {self.model}
              \rYear: {self.year}
              \rColor: {self.color}
              ''')
        
    def new_color(self, color):
        self.color = color
        
c1 = Car('Benz', 'S200', 2026)
c2 = Car('BMW', 'Sport', 2025)
c3 = Car('WW', 'Shasi', '2026')

c1.new_color('White')
c1.attribute()
=======
import tools

print(tools.add(5,6))
>>>>>>> f5fdf1c30efb54ace9fc2ccd438aacc1344a5461
