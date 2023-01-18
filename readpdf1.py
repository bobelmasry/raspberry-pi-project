from PyPDF2 import PdfReader 
from PIL import Image, ImageGrab
from pdftest import output
subject = 'eco'
subjectCode = '9708'
paperNumber = 1
pdfPath = r"C:\Users\donat\Documents\python_projects\Teachmegcse\teachmegcse3\Teachmegcse1\past_papers\static\past_papers\9708\9708_m16_qp_12.pdf"
output1Path = r"C:\Users\donat\Documents\python_projects\output1"
pdfName = '9708_m16_qp_12'

currentQuestion = 1
numOfQuestions = 30
reader = PdfReader(pdfPath)
f = open(f"{output1Path}/{subject}/p{paperNumber}/numofquestions.txt",'r')
initial = f.read()
f.close()
f = f = open(f"{output1Path}/{subject}/p{paperNumber}/numofquestions.txt",'w')
output(pdfPath,f"{output1Path}/{subject}/p{paperNumber}",pdfName)
numberOfPages = reader.getNumPages()
for i in range(numberOfPages - 2):
    i = i + 1
    page = reader.pages[i]
    text = page.extract_text()
    firstQuestion = True
    #while to check if question is in page
    #if to set start pixel to top of page if first question
    while page.extract_text().find('%s' %i) != -1:
        if firstQuestion == True:
            prevPixel = 0
        else:
            prevPixel = currentPixel
        currentPixel = page.extract_text().find('%s ' %currentQuestion)
        
        Image.open(f"{output1Path}/{subject}/p{paperNumber}/{pdfName}/{i}_{pdfName}.pdf.jpg")
        im = ImageGrab.grab(bbox=(300, prevPixel, 1300, currentPixel))
        current = int(initial) + currentQuestion
        current = str(current)
        im.save(f"C:/Users/donat/Documents/python_projects/output/{subjectCode}/p{paperNumber}/{subject}_{current}.jpg")
        first_question = False
        currentQuestion +=1
        
        final = int(initial) + numOfQuestions
        final = str(final)
        f.write(final)
        f.close()
    print(text)