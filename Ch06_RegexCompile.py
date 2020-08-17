import re

text = "Todays date 2020-08-18. Another date is 1996/02/11. The last date to remember is 1996-10-05"

match = re.compile(r"\d{4}[-/]\d{2}[-/]\d{2}")
match2 = re.compile(r"(\d{4})[-/](\d{2})[-/](\d{2})")

result = match.findall(text)
print(result)

# splits into each digit
result = match2.findall(text)
print(result)

text2 = "this is a new date: 2015-02-24"
newresult1 = match.findall(text2)
newresult2 = match2.findall(text2)

print(newresult1)
print(newresult2)
