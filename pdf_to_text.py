from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from io import BytesIO

import warnings
Image.MAX_IMAGE_PIXELS = None
warnings.simplefilter('ignore', Image.DecompressionBombWarning)

PDF_file = "./file.pdf"

print("Reading PDF...")
pages = convert_from_path(PDF_file, 1000)

final_text = ""

for index, page in enumerate(pages):
    print("Processing Page " + str(index) + "...")
    image = BytesIO()
    page.save(image, 'JPEG') 
    image.seek(0, 0)
    text = str(pytesseract.image_to_string(Image.open(image), config='-psm 6'))
    text = text.replace('-\n', '')     
    final_text += text

print(final_text)

with open("out_text.txt", "w", encoding='utf-8') as f:
    f.write(final_text)