import requests

url = "http://example.com/"

response = requests.get(url)

# directly gives content
print(response.content)
print(type(response.content))  # returns byte
print("------------------")

# gives with spacing
print(response.text)
html = response.text
print(type(response.text))  # returns string

with open("download.html", "w") as file:
    file.write(html)