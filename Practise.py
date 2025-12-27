class Car:
    def __init__(self, year, brand):
        self.year = year
        self.brand = brand

    def show(self):
        print(f'Brand: {self.brand}, Year: {self.year}')


x = Car(1442, 'Benz')
x.show()