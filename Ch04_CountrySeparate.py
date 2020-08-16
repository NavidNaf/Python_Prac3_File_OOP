with open("countries.txt", "r") as file:
    countryByL = dict()
    countryLs = []
    for line in file:
        countryLs.append(line)
    for i in range(len(countryLs)):
        countryByL[countryLs[i][0]] = countryByL.get(
            countryLs[i][0], 0) + 1
    print(countryByL)
    for i in countryByL.keys():
        with open(i+".txt", "w") as newFile:
            for j in range(len(countryLs)):
                if countryLs[j][0] == i:
                    newFile.write(countryLs[j])
