from dataclasses import dataclass, asdict
import json

@dataclass

class Product:
    name: str
    price: int
    in_stock: bool

product1 = Product("Leptop", 500, True)
product2 = Product("Phone", 300, True)
product3 = Product("Camera", 200, False)

product_list = asdict(product1), asdict(product2), asdict(product3)
json_data = json.dumps(product_list, indent=4)
print(json_data)