import re

email = "This is a random email address: navidnaf@outlook.com navidnaf@outlook thank you"

email2 = "A bunch of email address: navid.naf@outlook.com, navid_naf@outlook.com, navidnaf@outlook.com"

match = re.findall(r"\w+@\w+\.\w+", email)
match2 = re.findall(r"[.\w]+@\w+\.\w+", email2)
# [.\w]+ -> (.) may or may not ., (\w) words after that, (+) more.

print(match)
print(match2)
