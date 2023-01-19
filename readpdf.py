from PyPDF2 import PdfReader 
from PIL import Image
from pdf2image import convert_from_path    #import library

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
y = open(f"{output1Path}/{subject}/p{paperNumber}/numofpages.txt",'r')
initialPage = y.read()
y.close()
y = open(f"{output1Path}/{subject}/p{paperNumber}/numofpages.txt",'w')
f = open(f"{output1Path}/{subject}/p{paperNumber}/numofquestions.txt",'w')
images = convert_from_path(pdfPath, poppler_path= r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin') #Read pdf file
for x in range(len(images)):
    images[x].save(f"{output1Path}/{subject}/p{paperNumber}/{x + int(initialPage)}.jpg", 'JPEG')  #Convert each page into image and save it to the directory
    finalPage = int(initialPage) + x
y.write(str(finalPage))
y.close()

numberOfPages = reader.getNumPages()
for i in range(numberOfPages - 2):
    i = i + 1
    page = reader.pages[i]
    text = page.extract_text()
    firstQuestion = True
    #while to check if question is in page
    #if to set start pixel to top of page if first question
    while page.extract_text().find('%s' %currentQuestion) != -1:
        if firstQuestion == True:
            prevPixel = 0
        else:
            prevPixel = currentPixel
        
        currentPixel = page.extract_text().find('%s' %currentQuestion)
        with Image.open(f"{output1Path}/{subject}/p{paperNumber}/{i + int(initialPage)}.jpg") as im:
            im_crop = im.crop((300, prevPixel, 1300, currentPixel))
            current = int(initial) + currentQuestion
            current = str(current)
            im_crop.save(f"C:/Users/donat/Documents/python_projects/output/{subjectCode}/p{paperNumber}/{subject}_{current}.jpg")
            first_question = False
            currentQuestion +=1
            
            final = int(initial) + numOfQuestions
            final = str(final)
            f.write(final)
            f.close()
    i += 1
    print(text)