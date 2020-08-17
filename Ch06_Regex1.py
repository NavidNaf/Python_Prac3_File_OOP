import re

country = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Nederlands, New Zealand, Sweden, Switzerland"

li = re.findall(r'(\w+lands*)', country)
print(li)
