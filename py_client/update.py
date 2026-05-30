import requests


endpoint = "http://127.0.0.1:8000/products/4/update/"

data = {
    "title": "col",
    "price": 123.33,
}

get_response = requests.put(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())
