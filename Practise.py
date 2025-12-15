class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self):
        product_name = input('type name product: ')
        stock = int (input('Initial warehouse inventory: '))
        
        if product_name in self.products:
            self.products[product_name] += stock
        else:
            self.products[product_name] = stock

    def reduce_stock(self):
        product_name = input('type name product: ')
        if product_name not in self.products:
            print('error')
            return
        
        amount = int (input('type amount: '))
        if amount > self.products[product_name]:
            print('Not Find')
            return
        
        else:
            self.products[product_name] -= amount
            print(f'{amount} units removed from {product_name}')

    def show_products(self):
        for product_name , stock in self.products.items():
            print(f'Product: {product_name}, Stock: {stock}')