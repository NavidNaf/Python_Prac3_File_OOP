import requests

url = "https://github.com/NavidNaf"

response = requests.get(url)

print(type(response))

# is the response working
print(response.ok)

# what's the status code of the response
print(response.status_code)

# what does it mean
print(response.reason)
