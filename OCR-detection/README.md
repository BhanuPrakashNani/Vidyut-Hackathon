# Optical Character Recognition

## What is OCR?

Optical Character Recognition(OCR) is the process of electronically extracting text from images or any documents like PDF and reusing it in a variety of ways such as full text searches.


## pytesseract:

It will recognize and read the text present in images. It can read all image types — png, jpeg, gif, tiff, bmp etc. It’s widely used to process everything from scanned documents.

## Installation:

$ sudo pip install pytesseract

## Requirements:

* Requires python 2.5 or later versions.
* And requires Python Imaging Library(PIL).

## Usage:

From the shell:

$ ./pytesseract.py test.png

Above command prints the recognized text from image ‘test.png’.

$ ./pytesseract.py -l eng test-english.jpg

Above command recognizes english text.
