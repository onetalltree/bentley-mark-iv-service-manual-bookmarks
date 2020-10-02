# bentley-mark-iv-service-manual-bookmarks

Bookmarks for the Bentley VW Jetta, Golf, GTI, Mark IV Service Manual 1999 - 2005

This repository contains the files necessary to add a clickable table of contents/bookmarks to the OCRd Bentley Jetta, Golf, GTI 1999-2005 Service Manual.
This manual covers 1.8L turbo, 1.9L TOI and PO diesel, 2.0L gasoline, 2.8L VR6 on the A4 Platform.

Bookmarks can be managed using the Excel spreadsheet and then exported to a text file. PDFTk is then used to add the bookmarks to the PDF.

NOTE: Due to copyright issues, the PDF is not included in this repository.

## Directory Structure

```General
.../BENTLEY-MARK-IV-SERVICE-MANUAL-BOOKMARKS
├───build
├───definitions
│   ├───Additional
│   ├───Index
│   └───TableOfContents
```

* definitions: contains the raw and processed definitions files
  * TableOfContents: contains definitions for the table of contents
  * Index: contains defintions for the index
  * Additional: contains definitions for places of interest

* build: contains files in the PdfTk bookmark format

* The final bookmark file needed by PdfTk is stored in the root, called "bookmarks.txt"

## Build system

Bookmarks are stored in CSV files for easy editing. The csv files are convered to JSON files for easy processing by other programs. The JSON files are converted into the actual bookmark format needed by PdfTk. The individual bookmark files are combined into a single file which is process by PdfTk.

The build system is managed by a Makefile stored in the root directory.

* Tested on Linux
* Requires python3 for interpolated string.

## Adding the bookmarks to a PDF

Due to copyright, the actual PDF is not available in this repository.

Use the script or the command in the Powershell script "add_bookmarks_to_pdf.ps1" to add the bookmarks into your PDF.

* The script expects the bookmarks file and the pdf file to be in the same directory.
* It expects the pdf to be named "Bentley_VolkswagenJettaGolfGTI_MK4ServiceManual_1999-2005.pdf"
* It expects the bookmarks file to be named "bookmarks.txt"

PdfTk requires that the bookmarks.txt file be in Ascii (not unicode). If it generates the message:

```pdftk Warning: unexpected case 1 in LoadDataFile(); continuing```

then the bookmarks.txt file is likely was built improperly and in the wrong format. This can be fixed by opening the file using a text editor and saving with Ascii/Ansi format.

## PDF Files (not included in this repository due to copyright)

* Bentley_VolkswagenJettaGolfGTI_MK4ServiceManual_1999-2005.pdf
  * Source PDF file
* Bentley_VolkswagenJettaGolfGTI_MK4ServiceManual_1999-2005_Bookmarks.pdf
  * Output PDF file containing added bookmarks
