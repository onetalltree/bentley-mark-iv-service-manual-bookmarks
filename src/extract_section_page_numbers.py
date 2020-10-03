import sys
import json

jsonData = sys.stdin.read()

tocEntries = json.loads(jsonData)
sections = []

for tocEntry in tocEntries:
    if tocEntry["sectionNumber"] != None and tocEntry["sectionPageNumber"] == None:
        try:
            pdfPageNumber = int(tocEntry["pdf_page"])
            s = { "sectionNumber":tocEntry["sectionNumber"], "pdfPageNumber":pdfPageNumber}
            sections.append(s)
        except:
            pass

print(json.dumps(sections,indent=4))