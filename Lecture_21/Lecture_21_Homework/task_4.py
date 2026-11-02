import requests

Base_URL = "https://crudcrud.com/api/dc095d6c4b7a45c0833b2af63a4a8095"

def update_product():
    updated_product = {"name": "Gaming Leptop",
                       "price": 3200,
                       "in_stock": True
    }                       
    response = requests.put(f"{Base_URL}/products/6ae75c038db06403e88f61f4",
                            timeout=10, 
                            json=updated_product
    )
    response.raise_for_status()
    print(response.status_code)

    updated_response = requests.get(f"{Base_URL}/products/6ae75c038db06403e88f61f4",
                                    timeout=10,
                                    json=updated_product
    )
    updated_response.raise_for_status()
    updated_data = updated_response.json()
    print(updated_data)

update_product()