class Product:
    shop_name = "Megashop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        print("-" * 40)
        print(f"Product name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        self.stock -= quantity
        print(f"Sold: {quantity} {self.name}, remaining: {self.stock}")

product1 = Product("Leptop", 200, 8)
product1.sell(3)
product2 = Product("Camera", 100, 5)
product2.sell(1)
product3 = Product("Phone", 90, 7)
product3.sell(2)