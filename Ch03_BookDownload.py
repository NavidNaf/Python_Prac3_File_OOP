import sys
import requests

firstPortion = "http://subeen.com/download/"
secondPortion = "process.php"

totalUrl = firstPortion + secondPortion

info = {
    "name": "Karim",
    "email": "navid.naf@outlook.com",
    "country": "Mouri-Tania"
}

response = requests.post(totalUrl, data=info)

if response.ok == False:
    exit("Error Downloading the File")

with open("book.pdf", "wb") as book:
    book.write(response.content)

print("Download Complete.")
