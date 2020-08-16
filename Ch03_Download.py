import requests

url = "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiUzZ2DiZ_rAhUiwjgGHfKmAzYQFjADegQIBxAB&url=http%3A%2F%2Fwww.pdf995.com%2Fsamples%2Fpdf"

response = requests.get(url)

with open("file.pdf", "wb") as file:
    file.write(response.content)
