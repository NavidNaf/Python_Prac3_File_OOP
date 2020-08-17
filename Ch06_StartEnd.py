import re

text = "Bangla english Bangla"

match = re.findall(r"english", text)
print(match)

match = re.findall(r"^english", text)
print(match)

print("----------")

match = re.findall(r"^Bangla", text)
print(match)

match = re.findall(r"^bangla", text)
print(match)

match = re.findall(r"Bangla$", text)
print(match)

match = re.findall(r"bangla$", text)
print(match)

print("----------")

match = re.findall(r"^Bangla", text, re.I)
print(match)

match = re.findall(r"^bangla", text, re.I)
print(match)

match = re.findall(r"Bangla$", text, re.I)
print(match)

match = re.findall(r"bangla$", text, re.I)
print(match)
