from dataclasses import dataclass, field

@dataclass

class Product:
    name: str
    price: int
    in_stock: bool

product1 = Product("Leptop", 500, True)
print(product1)

product2 = Product("Phone", 300, True)

print(product2)

product3 = Product("Camera", 200, False)
print(product3)