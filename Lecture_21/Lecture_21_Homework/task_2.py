import requests

Base_URL = "https://crudcrud.com/api/dc095d6c4b7a45c0833b2af63a4a8095"

def get_all_product():

    response = requests.get(f"{Base_URL}/products", timeout=10)
    response.raise_for_status()
    products = response.json()
    print(response.json())

    for product in products:
        print(f"Name: {product['name']}, Price: {product['price']}, ID: {product['_id']}")

get_all_product()