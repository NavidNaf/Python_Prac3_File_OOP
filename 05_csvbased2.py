import csv

with open("demo.csv", "r") as rf:
    rfRead = csv.DictReader(rf)

    with open("democopy.csv", "w") as wf:
        fieldnames = ["policyID", "statecode", "county"]
        wfWrite = csv.DictWriter(wf, fieldnames=fieldnames)

        wfWrite.writeheader()
        for line in rfRead:
            del line["eq_site_limit"]
            del line["hu_site_limit"]
            del line["fl_site_limit"]
            del line["fr_site_limit"]
            del line["tiv_2011"]
            del line["tiv_2012"]
            del line["eq_site_deductible"]
            del line["hu_site_deductible"]
            del line["fl_site_deductible"]
            del line["fr_site_deductible"]
            del line["point_latitude"]
            del line["point_longitude"]
            del line["line"]
            del line["construction"]
            del line["point_granularity"]
            wfWrite.writerow(line)
