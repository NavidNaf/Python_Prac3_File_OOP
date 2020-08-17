import re

match = re.search(".", "Bangladesh")
print(match.group())

match = re.search("B.n", "Bangladesh")
print(match.group())

match = re.search("B.n....", "Bangladesh")
print(match.group())

match = re.search("...................", "Bangladesh is my mother land")
print(match.group())

match = re.search("m\w\w\w\w\w", "Bangladesh is my mother land")
print(match.group())

match = re.search("B\w+", "Bangladesh is my mother land")
print(match.group())

match = re.search("m\w+h\w+", "Bangladesh is my mother land")
print(match.group())