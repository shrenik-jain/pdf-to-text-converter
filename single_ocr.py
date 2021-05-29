from PIL import Image
import pytesseract as pyt
from pytesseract import Output
from pdf2image import convert_from_path

import os
import sys


pdf_file = 'resources/resume.pdf'

# Store all the pages of the PDF in a variable
pages = convert_from_path(pdf_file , 500)

# Counter to store images of each page of PDF to image
image_count = 1

for page in pages:
    '''
    Declaring filename for each page of PDF as JPG
    For each page, filename will be:
    PDF page 1 -> page_1.jpg
    PDF page 2 -> page_2.jpg
    PDF page 3 -> page_3.jpg
    '''

    filename = "page_" + str(image_count) + ".jpg"
    page.save(filename, 'JPEG')
    image_count += 1

# Variable to get count of total number of pages
file_lmt = image_count - 1
output_file = "output_file.txt"
f = open(output_file , "a")

for i in range(1 , file_lmt + 1):
    filename = "page_" + str(i) + ".jpg"

    # Recognize the text as string in image using pytesserct
    text = str(((pyt.image_to_string(Image.open(filename)))))

    # String Preprocessing
    text = text.replace('-\n', '')    
    f.write(text)

f.close()