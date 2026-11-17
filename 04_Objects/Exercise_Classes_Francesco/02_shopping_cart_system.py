class ShoppingCart:

    def __init__(self):
        self.cart = []

    def add(self, product, quantity):
        for index, (cart_product, cart_quantity) in enumerate(self.cart):
            if cart_product is product:
                self.cart[index] = (cart_product, cart_quantity + quantity)
                return

        self.cart.append((product, quantity))

    def subtotal(self):
        return sum(
            product.get_price(quantity)
            for product, quantity in self.cart
        )

    def total(self):
        return sum(
            product.get_price(quantity) * (1 + Product.tax_rate)
            for product, quantity in self.cart
        )

    def __len__(self):
        return sum(quantity for el, quantity in self.cart)


class Product:

    tax_rate = 0.10

    def __init__(self, name, price):
        self.name = name
        self.price = price  
        
        
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    @classmethod
    def set_tax_rate(cls, rate):
        """Set the rate on this class; subclass values shadow, not change, parent values."""
        cls.tax_rate = rate

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            value = 0
        self._price = value

    def get_price(self, quantity):
        return self.price * quantity

class DiscountedProduct(Product):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_price(self, quantity):
        return super().get_price(quantity) * (1 - self.discount / 100)

class BulkProduct(Product):

    def __init__(self, name, price, min_quantity, bulk_discount):
        super().__init__(name, price)

        self.min_quantity = min_quantity
        self. bulk_discount = bulk_discount

    def get_price(self, quantity):
        if quantity >= self.min_quantity:
            return super().get_price(quantity) * (1 - self.bulk_discount / 100)
        return super().get_price(quantity)



laptop = Product("Laptop", 1000)
mouse = DiscountedProduct("Mouse", 50, 20)
notebook = BulkProduct("Notebook", 10, 5, 30)

cart = ShoppingCart()

cart.add(laptop, 1)
cart.add(mouse, 2)
cart.add(notebook, 6)

print(len(cart))        # 9
print(cart.subtotal())  # 1122.0
print(cart.total())     # 1234.2

laptop.price = -100

print(laptop.price)     # 0
print(cart.subtotal())  # 122.0