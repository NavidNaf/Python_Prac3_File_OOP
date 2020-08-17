import re

with open("exercise.html", "r") as file:
    readfile = file.read()

print(readfile)

result2 = re.findall(r"<li>(.*?)</li>", readfile, re.MULTILINE)
result = re.findall(r"<li>(.*?)<ol>", readfile)

for i in range(3):
    print(f"{result[i]} - {result2[2 * i]}, {result2[2 * i+1]}")
