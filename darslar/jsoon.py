import requests

x = requests.get("https://dummyjson.com/products")
data = x.json()
print(f'ismi: {data['name']}')
print(f"User-Name: {data['username']}")
print(data['email'])
print(data['address']['street'])
print(data['phone'])
print(data['address']['zipcode'])
print(f"website: {data['website']}")













