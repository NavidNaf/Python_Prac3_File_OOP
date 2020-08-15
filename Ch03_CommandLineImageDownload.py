from sys import argv
import requests

if len(argv) != 3:
    print("Usage: (python file.py) (image url) (file name)")

url = argv[1]
response = requests.get(url)

imageContent = response.content

with open(argv[2], "wb") as imageFile:
    imageFile.write(imageContent)