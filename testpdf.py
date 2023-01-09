from PyPDF2 import PdfReader 
from PIL import Image, ImageGrab


reader = PdfReader("example.pdf")
number_of_pages = reader.getNumPages()
for i in range(number_of_pages - 2):
    i = i + 1
    page = reader.pages[i]
    text = page.extract_text()
    first_question = True
    while page.extract_text().find('%s' %i) != -1:
        if first_question == True:
            prevPixel = 0
        else:
            prevPixel = currentPixel
        currentPixel = page.extract_text().find('%s' %i)
        im = ImageGrab.grab(bbox=(300, prevPixel, 1300, currentPixel))
        im.save('filename')
        first_question = False
    print(text)