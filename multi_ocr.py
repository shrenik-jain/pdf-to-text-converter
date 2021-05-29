from PIL import Image
import pytesseract as pyt
from pytesseract import Output
from pdf2image import convert_from_path

import os
import sys


image_path = 'images/'
text_path = 'text_files/'
pdf_path = 'resources/'

for pdf_file in os.listdir('resources/'):

    pdf_file = os.path.join(pdf_path , pdf_file)

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
        filename = os.path.join(image_path , filename)
        page.save(filename, 'JPEG')
        image_count += 1

    # Variable to get count of total number of pages
    file_lmt = image_count - 1

    # Creating a text file to write the output
    output_file = str(pdf_file) + "_output_file.txt"
    output_file =  output_file[10:].replace('.pdf' , '')
    output_file = os.path.join(text_path , output_file)


    # Open the file in append mode so that all contents of all images are added to the same file
    f = open(output_file , "a")

    for i in range(1 , file_lmt + 1):
        filename = "page_" + str(i) + ".jpg"
        filename = os.path.join(image_path , filename)

        # Recognize the text as string in image using pytesserct
        text = str(((pyt.image_to_string(Image.open(filename)))))

        # String Preprocessing
        text = text.replace('-\n', '')    
        f.write(text)

    f.close()