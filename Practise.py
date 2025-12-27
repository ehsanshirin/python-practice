class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hello{self.name} , with {self.age}')


p1 = Person('Ehsan',34)

p1.greet()