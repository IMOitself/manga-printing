# manga-printing
no tutorials yet but i will try to document as much as possible. **the guide is not yet recommended.**

## workflow
- go to a desired manga on [mangakatana.com](https://mangakatana.com/manga)
- select chapters to download as a zip (you can only download 10 chapters at once)
- extract each zip and combine their contents into one folder. (each subfolders inside (e.g c001) will be moved to 1 location)
<br>

- open paper_labels_maker.xlsx on google spreadsheet
- on Sheet 1. modify cell A1 to number of pages of the manga you will print
- go to Sheet 2. and File > Download > Comma Separated Value (.csv)
- you will get paper_labels_maker - Sheet 2.csv

- open [paperLabeled.indd](paperLabeled.indd) in adobe indesign
- go to Window > Utilities > Data Merge > (that small hamburger menu) > Select Data Source...
- find and select 'paper_labels_maker - Sheet 2.csv" that you downloaded earlier

[TODO: Adding images from the manga]

- to print go to File > Print Booklet > Print

TODO: simplify all this process
