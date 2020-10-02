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

indexSourceData = json.loads(jsonData)

print('BookmarkBegin')
print(f"BookmarkTitle: Index")
print(f'BookmarkLevel: 1')
print(f'BookmarkPageNumber: ')

for data in indexSourceData:
    if data["type"]=='section':
        print('BookmarkBegin')
        print(f"BookmarkTitle: {data['section_name']}")
        print(f'BookmarkLevel: 2')
        print(f'BookmarkPageNumber: ')
    elif data["type"]=='index':
        print('BookmarkBegin')
        print(f"BookmarkTitle: {data['section_name']} [{data['sectionNumber']} - {data['sectionPageNumber']}]")
        print(f'BookmarkLevel: 2')
        print(f'BookmarkPageNumber: ')
    elif data["type"]=='no numbering':
        print('BookmarkBegin')
        print(f"BookmarkTitle: {data['section_name']}")
        print(f'BookmarkLevel: 2')
        print(f'BookmarkPageNumber: ')
    elif data["type"]=='see':
        print('BookmarkBegin')
        print(f"BookmarkTitle: see: {data['reference']}")
        print(f'BookmarkLevel: 3')
        print(f'BookmarkPageNumber: ')
    elif data["type"]=='see also':
        print('BookmarkBegin')
        print(f"BookmarkTitle: see also: {data['reference']}")
        print(f'BookmarkLevel: 3')
        print(f'BookmarkPageNumber: ')
    else:
        print(f'Line {data["line"]}: unexpected type {data["type"]}', file=sys.stderr)