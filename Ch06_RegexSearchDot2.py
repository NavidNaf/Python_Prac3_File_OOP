import re

match = re.search("B.+", "Bangladesh is my mother land")
print(match.group())

match = re.search("B.+h", "Bangladesh is my mother land")
print(match.group())

match = re.search("B.+?h", "Bangladesh is my mother land")
print(match.group())

match = re.search("B.+?", "Bangladesh is my mother land")
print(match.group())