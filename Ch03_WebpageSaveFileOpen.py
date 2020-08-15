import requests
import os
import webbrowser as wb

# fetch the html file
url = "http://www.blueriverfinancial.com.au/"

response = requests.get(url)
htmlStr = response.text

# copying the webpage to a file
with open("blueriv.html", "w") as file:
    file.write(htmlStr)

filePath = os.path.realpath("blueriv.html")
fileName = "file://" + filePath
wb.open(fileName)
