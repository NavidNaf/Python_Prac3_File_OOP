import re

s = "Abcd 1432-1045"
result = re.sub(r"\d", "0", s)
print(result)
