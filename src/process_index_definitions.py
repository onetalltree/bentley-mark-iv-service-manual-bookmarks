import sys
import json
import re

# Synopsis

def remove_prefix(string, prefix):
    if string.find(prefix, 0) == 0:
        string = string[len(prefix):]

    return string


# get the section-page from the line, if present
# returns a tuple (section number, section page number, match start)

def get_document_page_numbers(line):
    # TODO: force regex to end of line
    match = re.search(r"\w+-\d+", line)

    if match is None:
        return (False, None, None, None)
    else:
        d = match.group().split('-')
        return (True, d[0], d[1], match.start())


def process_definitions(definitions_file, section_page_numbers):
    index = []
    line_number = 0

    for line in definitions_file:
        line_number += 1
        line = line.strip()

        (numbering_available, section_number, section_page_number, match_start) = get_document_page_numbers(line)

        # Process definition

        o = None

        if len(line) == 1:
            o = {"lineNumber": line_number, "type": "section_letter",
                "text": line.upper()}
        elif line.find("see also ", 0) == 0:
            o = {"lineNumber": line_number, "type": "see_also",
                "text": remove_prefix(line, "see also").strip()}
        elif line.find("see ", 0) == 0:
            o = {"lineNumber": line_number, "type": "see",
                "text": remove_prefix(line, "see").strip()}
        elif numbering_available:
            o = {"lineNumber": line_number, "type": "reference",
                "text": line[0:match_start].strip(),
                "sectionNumber": section_number, "sectionPageNumber": section_page_number}

            if section_number in section_page_numbers.keys():
                pdf_page_number = section_page_numbers[section_number] + int(section_page_number)-1
                o["pdfPageNumber"] = pdf_page_number
        else:
            o = {"lineNumber": line_number, "type": "heading",
                "text": line.strip()}

        if o is not None:
            index.append(o)

    return index


def main():
    sectionPageNumberFileName = sys.argv[1]
    sectionPageNumberFile = open(sectionPageNumberFileName, "r")
    sectionPageNumbers = json.loads(sectionPageNumberFile.read())

    index = process_definitions(sys.stdin, sectionPageNumbers)
    print(json.dumps(index, indent=4))


if __name__ == "__main__":
    main()
