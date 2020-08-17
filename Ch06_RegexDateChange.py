import re

date = "22/07/2017, 18/08/2020, 05/10/2015"

result = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", date)

print(result)
