import csv
import json
import sys

reader = csv.DictReader(sys.stdin)

bookmarks = []
line_number = 0

for row in reader:
    line_number += 1

    sectionPageNumberRaw = row["PageNumName"].strip()
    sectionNumbers = sectionPageNumberRaw.split("-")
    sectionNumber = sectionNumbers[0].strip() if len(sectionNumbers)>=1 else None
    sectionPageNumber = sectionNumbers[1].strip() if len(sectionNumbers)>=2 else None

    o = {
        "line" : line_number,
        "type" : "toc_entry",
        "toc_level" : row["Level"],
        "toc_description" : row["Title"],
        "sectionNumbers" : sectionPageNumberRaw,
        "sectionNumber" : sectionNumber,
        "sectionPageNumber" : sectionPageNumber,
        "pdfPageNumber" : row["Page"] }

    bookmarks.append(o)

print(json.dumps(bookmarks, indent=4))
