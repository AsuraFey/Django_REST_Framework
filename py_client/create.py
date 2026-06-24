import requests

headers = {"Authorization": 'Bearer 6a9eb2a2a982ae6fcd189d93dbb116fbcf7a94ee'}
endpoint = "http://127.0.0.1:8000/products/"


data = {
    'title': 'algo2',
    # 'content':'',
    'price': 32.99,
    # 'sale_price':,
    # 'discount':,
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.status_code)
print(get_response.json())
