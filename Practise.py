class Shop:
    def __init__(self):
        pass

    def add_product(self, product_name, stock, price):
        pass

    def reduce_stock(self, product_name, amount):
        pass

    def show_list(self):
        pass
        



class Custumer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def show_order(self):
        print(f'Orders fo {self.name}:')
        for order in self.orders:
            print(order)


class Order:
    def __init__(self, custumer, product_name, amount):
        self.custumer = custumer
        self.pruduct_name = product_name
        self.amount = amount
        
    
    def __str__(self):
        return f'{self.custumer.name} order {self.amount} of {self.pruduct_name}'