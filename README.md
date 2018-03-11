## ISBN-Scan

Build a home library catalog by scanning (or manually entering) ISBNs

## Usage

Put input files in the "input" folder. (There have to be at least two input files.) Filnames can be anything, but should probably be location-based (e.g. "bedroom-left-shelf.txt").

Each line in an input file is a book, either an ISBN (with or without the 978 prefix), or as

    Title,Lastname,Firstname,Year,Publisher(,ISBN or other identifier -- optional)

To add books from an input file to the database, retrieving information from WorldCat:

    python3 verify.py input/something.txt

Verify.py can also be used to check for wrong or unknown ISBNs:

    python3 verify.py books.txt --noweb | fgrep "<<" | nl

Create the HTMl and CSV reports (output.html / output.csv):

    python3 report.py

## Prerequisites

* [isbnlib](https://github.com/xlcnd/isbnlib)
* grep
