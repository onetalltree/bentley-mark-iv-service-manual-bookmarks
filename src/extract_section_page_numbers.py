import sys
import json


def extract_section_starting_pages(toc_definitions):
    section_starting_pages = {}

    for toc_definition in toc_definitions:
        if toc_definition["sectionNumber"] is not None and toc_definition["sectionPageNumber"] is not None:
            try:
                pdf_page_number = int(toc_definition["pdfPageNumber"])
                section_number = toc_definition["sectionNumber"]

                # needs to check if already exists
                if section_number not in section_starting_pages.keys():
                    section_starting_pages[section_number] = pdf_page_number
                elif pdf_page_number < section_starting_pages[section_number]:
                    section_starting_pages[section_number] = pdf_page_number
            except:
                pass

    return section_starting_pages


def main():
    toc_definitions_json = sys.stdin.read()
    toc_definitions = json.loads(toc_definitions_json)

    section_starting_pages = extract_section_starting_pages(toc_definitions)

    print(json.dumps(section_starting_pages, indent=4))


if __name__ == "__main__":
    main()
