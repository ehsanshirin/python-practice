class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, stock):
        if product_name in self.products:
            self.products[product_name] += stock
        else:
            self.products[product_name] = stock

    def reduce_stock(self, product_name, amount):
        if product_name not in self.products:
            print(f'{product_name} not find')
            return

        if self.products[product_name] < amount:
                print(f'There is not enough inventory for {product_name}.')
                return
    
        self.products[product_name] -= amount
        print(f'{amount} units removed from {product_name}')

    def get_stock(self, product_name):
        if product_name not in self.products:
            print(f'{product_name} not find')
            return None
        return self.products[product_name]
    
    def show_products(self):
        for product_name , stock in self.products.items():
            print(f'Product: {product_name}, Stock: {stock}')

shop = Shop()

shop.add_product('Apple', 50)
shop.add_product('Banana', 40)

shop.show_products()

shop.reduce_stock('Apple', 20)
shop.reduce_stock('Banana', 50)

print(f'Stock of Apple: {shop.get_stock('Apple')}')
print(f'Stock of Banana: {shop.get_stock('Banana')}')

shop.show_products()