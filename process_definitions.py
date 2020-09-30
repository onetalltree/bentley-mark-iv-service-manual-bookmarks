import csv
import sys

reader = csv.DictReader(sys.stdin)

for row in reader:
    print(f'BookmarkBegin')

    title = row["Title"]

    if row["PageNumName"].strip():
        title = row["PageNumName"].strip() + " ... " + title

    print(f'BookmarkTitle: {title}')
    print(f'BookmarkLevel: {row["Level"]}')
    print(f'BookmarkPageNumber: {row["Page"]}')
