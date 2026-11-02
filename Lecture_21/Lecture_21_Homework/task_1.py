import requests


Base_URL = "https://crudcrud.com/api/dc095d6c4b7a45c0833b2af63a4a8095"


def add_product(product_data):
    
    response = requests.post(f"{Base_URL}/products", json=product_data, timeout=10)
    response.raise_for_status()
    print(response.json())

product1 = {"name": "Laptop", 
                "price": 2500, 
                "in_stock": True
}

product2 = {"name": "Camera",
            "price": 3000,
            "in_stock": True
}

product3 = {"name": "Phone",
            "price": 2300,
            "in_stock": True
}

add_product(product1)
add_product(product2)
add_product(product3)