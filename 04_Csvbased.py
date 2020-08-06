import csv

with open("demo.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile)

    with open("democopy.csv", "w") as newFile:
        csvWriter = csv.writer(newFile, delimiter="\t")

        for line in csvReader:
            csvWriter.writerow(line)
