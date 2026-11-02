import requests

Base_URL = "https://crudcrud.com/api/dc095d6c4b7a45c0833b2af63a4a8095"

def delete_product():
    response = requests.delete(f"{Base_URL}/products/6ae75a4a8db06403e88f61f3", timeout=10)
    response.raise_for_status()
    print(response.status_code)
    print("Product deleted successfully")

delete_product()
