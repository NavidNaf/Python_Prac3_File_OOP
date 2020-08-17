import re

digit = re.search("\d", "My Phone Number: 01706319096")
print(digit.group())

digit = re.search("\d+", "My Phone Number: 01706319096")
print(digit.group())

digit = re.search("\d+", "My House Number: 24, My Phone Number: 01706319096")
print(digit.group())

digit = re.search(
    "\d{11}", "My House Number: 24, My Phone Number: 01706319096")
print(digit.group())

digit = re.search(
    "\d{3}\s*\d{8}", "My House Number: 24, My Phone Number: 01706319096")
print(digit.group())
