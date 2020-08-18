import re

email = "book at subeen.com, book At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com "

email = re.sub(r"\s+[\(\[]*\s*at\s*[\)\]]*\s+", "@", email, flags=re.I)
print(email)
email = re.sub(r"\s+[\[]*\s*dot\s*[\]]*\s+", ".", email)
print(email)
