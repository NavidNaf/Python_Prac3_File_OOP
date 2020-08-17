import re

match = re.search("desh", "Bangladesh")
print(match)
print(match.group())

match = re.search("Bangla", "Bangladesh")
print(match.group())

match = re.search("dets", "Bangladesh")
print(match)
print(type(match))
print(match.group())
