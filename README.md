# python-pdf-table-to-excel
Extract data from irregular PDF table do excel.

Extract data from an irregular table from PDF format (e.g. technical drawing) into an Excel spreadsheet. 
The code works by entering annotations of all the fields that you want to extract into the PDF and then writing them as name : value pairs into the columns of the Excel workbook.

Attention, the fields must always be in the same place in the document - check visually!

The first and second files are auxiliary - it serves to visually identify all fields that we want to extract (so that the coordinates are known).
In the second file, the data is logged into the console for control.
The third file goes through all annotated PDFs and extracts data into an Excel spreadsheet.
