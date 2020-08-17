country = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Nederlands, New Zealand, Sweden, Switzerland"

counrtyList = country.split(",")
# forgot split, later remembered, so practice.
# print(counrtyList)

countryLand = []
for country in counrtyList:
    if country.endswith("land"):
        countryLand.append(country)

countryLand2 = [country for country in counrtyList if country.endswith(
    "land") or country.endswith("lands")]

print(countryLand)
print(countryLand2)
