import pytesseract
from PIL import Image

# Path to the Tesseract executable (update this if it's not in your system PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Open the image using PIL (Python Imaging Library)
image = Image.open('modules/tesserac/image.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)