import requests


endpoint = "http://127.0.0.1:8000/products/"


data = {
    'title': 'algo2',
    # 'content':'',
    'price': 32.99,
    # 'sale_price':,
    # 'discount':,
}

get_response = requests.post(endpoint, json=data)

print(get_response.status_code)
print(get_response.json())
