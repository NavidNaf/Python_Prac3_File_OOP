import re

ls = "<li>Naf</li><li>Navid</li><li>Fazle</li><li>Rabbi</li><li>Rocky</li>"

match = re.findall(r"<li>(.+?)</li>", ls)
print(match)
