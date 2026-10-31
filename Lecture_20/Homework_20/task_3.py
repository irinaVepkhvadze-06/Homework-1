import json

json_str = '{"name": "Laptop", "price": 2500, "in_stock": true}'

python_data = json.loads(json_str)
print(python_data)

class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

p = Product(**python_data)
print(type(p))
print(p.name)

