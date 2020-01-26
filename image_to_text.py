from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from io import BytesIO

import warnings
Image.MAX_IMAGE_PIXELS = None
warnings.simplefilter('ignore', Image.DecompressionBombWarning)

image = Image.open("./captcha.jpg")
image = image.convert('1')
image.show()
text = str(pytesseract.image_to_string(image, config='-psm 6'))
text = text.replace('-\n', '')     

print(text)