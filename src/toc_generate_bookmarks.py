import csv
import sys
import json

"""     o = {
        "line" : line_number,
        "type" : "toc_entry",
        "toc_level" : row["Level"],
        "toc_description" : row["Title"],
        "document_page" : row["PageNumName"].strip(),
        "pdf_page" : row["Page"] }
 """

jsonData = sys.stdin.read()

bookmarkDefinitions = json.loads(jsonData)

for bookmarkDef in bookmarkDefinitions:
    print('BookmarkBegin')

    if bookmarkDef["type"] == "toc_entry":
        title = bookmarkDef["toc_description"]

        if bookmarkDef["document_page"].strip():
            title = bookmarkDef["document_page"].strip() + " ... " + title

        print(f"BookmarkTitle: {title}")
        print(f'BookmarkLevel: {bookmarkDef["toc_level"]}')
        print(f'BookmarkPageNumber: {bookmarkDef["pdf_page"]}')
    else:
        print(f'Line {bookmarkDef["line"]}: unexpected bookmark type {bookmarkDef["type"]}', file=sys.stderr)