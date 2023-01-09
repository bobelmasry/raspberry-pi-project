from PyPDF2 import PdfReader 
from PIL import Image, ImageGrab

currentQuestion = 1
reader = PdfReader("example.pdf")
numberOfPages = reader.getNumPages()
for i in range(numberOfPages - 2):
    i = i + 1
    page = reader.pages[i]
    text = page.extract_text()
    firstQuestion = True
    while page.extract_text().find('%s' %i) != -1:
        if firstQuestion == True:
            prevPixel = 0
        else:
            prevPixel = currentPixel
        currentPixel = page.extract_text().find('%s ' %currentQuestion)
        im = ImageGrab.grab(bbox=(300, prevPixel, 1300, currentPixel))
        im.save('filename.jpg')
        first_question = False
        currentQuestion += 1
    print(text)