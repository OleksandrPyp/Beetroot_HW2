#Task 3 Product store
class Product:
    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.product_list = list()
        #self.product_price = self.amount * 1.3

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("This number should be grater than 0")
        quantity = self.product_list.append((product, amount))
        return quantity

    def set_discount(self, identifier, percent, identifier_type="name"):
        if percent < 0 or percent > 100:
            raise ValueError("Discount should be between 1 and 100%")
        if identifier_type == "name":
            product_list = [p for p in self.product_list if p[1] == identifier]
        elif identifier_type == "type":
            product_list = [p for p in self.product_list if p[0] == identifier]
        else:
            raise ValueError("Identifier should be either 'name' or 'type'")
        for p in product_list:
            p[2] *= (1 - percent/100)

    def sell_product(self, product_name, amount):
        pass

    def get_income(self):
        pass

    def get_all_products(self):
        pass

    def get_product_info(self, product_name):
        pass

p = Product('Sport', 'Football T-Shirt', 100)
s = ProductStore()

s.add(p, 10)
