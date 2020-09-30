# bentley-mark-iv-service-manual-bookmarks
Bookmarks for the Bentley VW Jetta, Golf, GTI, Mark IV Service Manual 1999 - 2005

This repository contains the files necessary to add a clickable table of contents/bookmarks to the OCRd Bentley Jetta, Golf, GTI 1999-2005 Service Manual.
This manual covers 1.8L turbo, 1.9L TOI and PO diesel, 2.0L gasoline, 2.8L VR6 on the A4 Platform.

Bookmarks can be managed using the Excel spreadsheet and then exported to a text file. PDFTk is then used to add the bookmarks to the PDF.

NOTE: Due to copyright issues, the PDF is not included in this repository.

## Data Files

* bookmark_definitions.csv
  * contains the bookmark definitions. 1 row per bookmark. Used to generate the bookmarks.txt file
* bookmarks.txt
  * contains the bookmark definitions used by PdfTk. Created from bookmark_definitions.csv file

## Programs

* process_definitions.py
  * Python program used to transform the bookmark_definitions.csv file into the bookmarks.txt file

## Scripts

* process_definitions.ps1
  * Powershell script used to run the process_definitions.py
* add_bookmarks_to_pdf.ps1
  * Powershell script used to run PdfTk to add the bookmarks to the PDF file

## PDF Files (not included in this repository due to copyright)

* Bentley_VolkswagenJettaGolfGTI_MK4ServiceManual_1999-2005.pdf
  * Source PDF file
* Bentley_VolkswagenJettaGolfGTI_MK4ServiceManual_1999-2005_Bookmarks.pdf
  * Output PDF file containing added bookmarks
