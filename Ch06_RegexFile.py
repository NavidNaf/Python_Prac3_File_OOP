import re

with open("test.txt", "r") as file:
    theFile = file.read()

lines = re.findall(r"^.+?$", theFile, re.M)
# (?) -> maybe there; if is there, not more than 1
print(lines)
