import sys
import json


def generate_bookmarks(bookmark_definitions):
    bookmark_lines = []

    for bookmark_definition in bookmark_definitions:
        bookmark_lines.append('BookmarkBegin')

        if bookmark_definition["type"] == "toc_entry":
            text = ""
            if bookmark_definition["sectionNumber"].strip():
                text = bookmark_definition["sectionNumber"].strip()
            if bookmark_definition["sectionPageNumber"].strip():
                text = text + "-" + bookmark_definition["sectionPageNumber"].strip()
            text = text + " ... " + bookmark_definition["text"]

            bookmark_lines.append(f"BookmarkTitle: {text}")

            bookmark_lines.append(f'BookmarkLevel: {bookmark_definition["level"]}')
            bookmark_lines.append(f'BookmarkPageNumber: {bookmark_definition["pdfPageNumber"]}')
        else:
            bookmark_lines.append(f'Line {bookmark_definition["lineNumber"]}: unexpected bookmark type {bookmark_definition["type"]}', file=sys.stderr)

    return bookmark_lines


def main():
    bookmark_definitions_json = sys.stdin.read()
    bookmark_definitions = json.loads(bookmark_definitions_json)

    bookmark_lines = generate_bookmarks(bookmark_definitions)
    print('\n'.join(bookmark_lines))


if __name__ == "__main__":
    main()
