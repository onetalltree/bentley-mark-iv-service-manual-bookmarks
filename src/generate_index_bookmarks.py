import sys
import json


def generate_bookmarks(bookmark_definitions):
    bookmark_lines = []

    bookmark_lines.append('BookmarkBegin')
    bookmark_lines.append(f"BookmarkTitle: Index")
    bookmark_lines.append(f'BookmarkLevel: 1')
    bookmark_lines.append(f'BookmarkPageNumber: ')

    for bookmark_definition in bookmark_definitions:
        pdf_page_number = bookmark_definition['pdfPageNumber'] if 'pdfPageNumber' in bookmark_definition.keys() else None

        if bookmark_definition["type"] == 'section_letter':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: {bookmark_definition['text']}")
            bookmark_lines.append(f'BookmarkLevel: 2')
            bookmark_lines.append(f'BookmarkPageNumber: ')
        elif bookmark_definition["type"] == 'heading':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: {bookmark_definition['text']}")
            bookmark_lines.append(f'BookmarkLevel: 3')
            bookmark_lines.append(f'BookmarkPageNumber: ')
        elif bookmark_definition["type"] == 'reference':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: {bookmark_definition['text']} ... {bookmark_definition['sectionNumber']}-{bookmark_definition['sectionPageNumber']}")
            bookmark_lines.append(f'BookmarkLevel: 4')
            if pdf_page_number is not None:
                bookmark_lines.append(f'BookmarkPageNumber: {pdf_page_number}')
            else:
                bookmark_lines.append(f'BookmarkPageNumber: ')
        elif bookmark_definition["type"]=='no numbering':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: {bookmark_definition['text']}")
            bookmark_lines.append(f'BookmarkLevel: 2')
            bookmark_lines.append(f'BookmarkPageNumber: ')
        elif bookmark_definition["type"]=='see':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: see: {bookmark_definition['text']}")
            bookmark_lines.append(f'BookmarkLevel: 4')
            bookmark_lines.append(f'BookmarkPageNumber: ')
        elif bookmark_definition["type"]=='see_also':
            bookmark_lines.append('BookmarkBegin')
            bookmark_lines.append(f"BookmarkTitle: see also: {bookmark_definition['text']}")
            bookmark_lines.append(f'BookmarkLevel: 4')
            bookmark_lines.append(f'BookmarkPageNumber: ')
        else:
            print(f'Line {bookmark_definition["lineNumber"]}: unexpected type {bookmark_definition["type"]}', file=sys.stderr)

    return bookmark_lines


def main():
    index_definitions_json = sys.stdin.read()
    index_definitions = json.loads(index_definitions_json)

    bookmark_lines = generate_bookmarks(index_definitions)
    print('\n'.join(bookmark_lines))


if __name__ == "__main__":
    main()
