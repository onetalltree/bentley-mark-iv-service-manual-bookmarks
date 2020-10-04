import csv
import json
import sys


def process_definitions(definition_file):
    reader = csv.DictReader(definition_file)

    bookmarks = []
    line_number = 0

    for row in reader:
        line_number += 1

        section_number = row["sectionNumber"]
        section_page_number = row["sectionPageNumber"]

        o = {
            "type": "toc_entry",
            "level": row["level"],
            "text": row["text"],
            "sectionNumber": section_number,
            "sectionPageNumber": section_page_number,
            "pdfPageNumber": row["pdfPageNumber"],
            "lineNumber": line_number
            }

        bookmarks.append(o)
    return bookmarks


def main():
    bookmarks = process_definitions(sys.stdin)
    print(json.dumps(bookmarks, indent=4))


if __name__ == "__main__":
    main()
