import csv
import re
from sys import argv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
else:
    # check csv
    checkCSV = argv[1].split(".")
    if checkCSV[1] != "csv":
        print("Usage: python dna.py data.csv sequence.txt")
        quit()

    # check txt
    checkTXT = argv[2].split(".")
    if checkTXT[1] != "txt":
        print("Usage: python dna.py data.csv sequence.txt")
        quit()

# csv
with open(argv[1], "r") as database:
    databaseReader = csv.reader(database)
    for i in databaseReader:
        titles = i
        break
    titles.pop(0)
    winLen = len(titles)

    # sequence / file
    seqDict = dict()
    with open(argv[2], "r") as sequence:
        buffer = sequence.read()
        for i in titles:
            m = 0
            to_find = i
            # did not understand, will understand later
            try:
                m = max(re.findall(r'(({})\2*)'.format(to_find), buffer),
                        key=lambda k: k[0])[0]
            except:
                print("No Match.")
                quit()
            seqDict[i] = str(len(m) // len(to_find))


# # print("------")
with open(argv[1], "r") as database:
    winner = None
    databaseDictReader = csv.DictReader(database)
    for i in databaseDictReader:
        count = 0
        # print(i)
        # print(i.get("name"))
        # print(seqDict)
        for head in titles:
            # print(i.get(head))
            # print("---")
            # print(seqDict.get(head))
            if i.get(head) == seqDict.get(head):
                count += 1
                # print(i.get("name"), count)
                if count == winLen:
                    winner = i.get("name")
    if winner == None:
        print("No match.")
    else:
        print(winner)
