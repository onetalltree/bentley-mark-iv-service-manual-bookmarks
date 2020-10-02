# import csv
import sys
import json

def remove_prefix(string, prefix):
    if string.find(prefix, 0) == 0:
        string = string[len(prefix):]

    return string

filename = "raw_copied_from_pdf.txt"

f = open(filename, "rt")

index = []
line_number = 0
previous_line = ""

for line in f:
    line_number+=1
    line = line.rstrip('\n')

    if len(line) == 1:
        o = { "line" : line_number, "type" : "section", "section_name" : line.upper()}
        index.append(o)
    elif line.find("see also ", 0) == 0:
        pass
    elif line.find("see ",0) == 0:
        o = {
            "line" : line_number,
            "type" : "see",
            "term" : previous_line,
            "reference" : remove_prefix(line, "see ")
        }
        index.append(o)

    previous_line = line

# print(json.dumps(index))
print("\n".join(index))