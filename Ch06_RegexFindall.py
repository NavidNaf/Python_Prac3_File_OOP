import re

numbers = "Some Phone Numbers: 017 06319096, 016 77250889, 01552408902, 00000000000, 123-123"

match = re.findall(r"\d{3}\s*\d{8}", numbers)
print(match)

match = re.findall(r"01[3456789]\s*\d{8}", numbers)
print(match)
