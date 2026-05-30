import requests

product_id = input("Product ID?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(" bad ")

if product_id:
    endpoint = f"http://127.0.0.1:8000/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code)
    print(get_response.json())
