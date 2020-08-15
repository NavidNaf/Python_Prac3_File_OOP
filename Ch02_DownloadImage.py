import requests

url = "https://scontent.fdac13-1.fna.fbcdn.net/v/t1.0-9/117444343_2652893864980209_4585492509959371182_n.jpg?_nc_cat=101&_nc_sid=8bfeb9&_nc_ohc=McA6Qc7cSpYAX-t6iSM&_nc_ht=scontent.fdac13-1.fna&oh=bbaaf7c0e57c2442872e69c6affa64fb&oe=5F5DB8C8"

response = requests.get(url)
imageByte = response.content

with open("image1.jpg", "wb") as imageFile:
    imageFile.write(imageByte)
