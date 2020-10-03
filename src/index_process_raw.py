import sys
import json
import re

# Synopsis

# index_process_raw <section page file> < raw
# Read the section page numbers
sections = {}

sectionPageNumberFile = open(sys.argv[1], "r")
sectionPageNumbers = json.loads(sectionPageNumberFile.read())

for s in sectionPageNumbers:
    try:
        pdfPageNumber = int(s["pdfPageNumber"])
        sections[s["sectionNumber"]] = pdfPageNumber
    except:
        pass


def remove_prefix(string, prefix):
    if string.find(prefix, 0) == 0:
        string = string[len(prefix):]

    return string

# get the section-page from the line, if present
# returns a tuple (section number, section page number, match start)
def get_document_page_numbers(line):
    match = re.search(r"\w+-\d+", line)

    if match==None:
        return None
    else:
        d = match.group().split('-')
        return (d[0], d[1], match.start())



index = []
line_number = 0

for line in sys.stdin:
    line_number+=1
    line = line.strip().replace('\t', ' ').replace('  ', ' ')

    # see if there is a page number

    numbering = get_document_page_numbers(line)
    numberingAvailable = numbering != None
    if numberingAvailable:
        sectionNumber = numbering[0]
        sectionPageNumber = numbering[1]
        matchStart = numbering[2]
    else:
        sectionNumber = None
        sectionPageNumber = None
        matchStart = None

    if len(line) == 1:
        o = { "line" : line_number, "type" : "section letter", "section_name" : line.upper() }
        index.append(o)
    elif line.find("see also ", 0) == 0:
        o = { "line" : line_number, "type" : "see also", "reference" : remove_prefix(line, "see also").strip() }
        index.append(o)
    elif line.find("see ",0) == 0:
        o = { "line" : line_number, "type" : "see", "reference" : remove_prefix(line, "see").strip() }
        index.append(o)
    elif numberingAvailable:
        o = { "line" : line_number, "type" : "index", "section_name" : line[0:matchStart].strip(), "sectionNumber":sectionNumber, "sectionPageNumber":sectionPageNumber}

        if sectionNumber in sections.keys():
            pdfPageNumber = sections[sectionNumber] + int(sectionPageNumber)-1
            o["pdfPageNumber"] = pdfPageNumber

        index.append(o)
    else:
        o = { "line" : line_number, "type" : "section", "section_name" : line.strip() }
        index.append(o)

print(json.dumps(index, indent=4))