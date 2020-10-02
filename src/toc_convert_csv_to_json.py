import csv
import json
import sys

reader = csv.DictReader(sys.stdin)

bookmarks = []
line_number = 0

for row in reader:
    line_number += 1

    o = {
        "line" : line_number,
        "type" : "toc_entry",
        "toc_level" : row["Level"],
        "toc_description" : row["Title"],
        "document_page" : row["PageNumName"].strip(),
        "pdf_page" : row["Page"] }

    bookmarks.append(o)

print(json.dumps(bookmarks, indent=4))
