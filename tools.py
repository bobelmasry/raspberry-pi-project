from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader

output1Path = r"C:\Users\donat\Documents\python_projects\output1"
pdfPath = r"C:\Users\donat\Documents\python_projects\Teachmegcse\teachmegcse3\Teachmegcse1\past_papers\static\past_papers\9708\9708_m16_qp_12.pdf"
images = convert_from_path(pdfPath, poppler_path= r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin')
subject = 'eco'
paperNumber = 1

def makeImages():
    initialPage = getInitial()[0]
    for x in range(len(images) - 2):
        x = x + 1
        images[x].save(f"{output1Path}/{subject}/p{paperNumber}/{x + int(initialPage)}.jpg", 'JPEG')  #Convert each page into image and save it to the directory
        finalPage = int(initialPage) + x
    y = open(f"{output1Path}/{subject}/p{paperNumber}/numofpages.txt",'r+')
    y.write(str(finalPage))
    y.close()

def getInitial():
    y = open(f"{output1Path}/{subject}/p{paperNumber}/numofpages.txt",'r+')
    f = open(f"{output1Path}/{subject}/p{paperNumber}/numofquestions.txt",'r+')
    initialQuestion = f.read()
    initialPage = y.read()
    y.close()
    f.close()
    values = [initialPage, initialQuestion]
    return values

def takeScreenshot(y1, y2, currentQuestion, i, subjectCode):
    initialQuestion = getInitial()[1]
    initialPage = getInitial()[0]
    with Image.open(f"{output1Path}/{subject}/p{paperNumber}/{i - 1 + int(initialPage)}.jpg") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            current = int(initialQuestion) + currentQuestion
            current = str(current)
            im_crop.save(f"C:/Users/donat/Documents/python_projects/output/{subjectCode}/p{paperNumber}/{subject}_{current}.jpg")

def numOfQuestionsInPage(currentPage, currentQuestion):
    currentPage -= 1
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    numOfQuestionsInPage = 0
    while page.extract_text().find(f"{currentQuestion} ") != -1:
        if page.extract_text().find(f"{currentQuestion} ") != -1:
            numOfQuestionsInPage += 1
            currentQuestion += 1
    return numOfQuestionsInPage

def saveFinal(finalQuestion, finalPage):
    f = open(f"{output1Path}/{subject}/p{paperNumber}/numofquestions.txt",'r+')
    f.write(finalQuestion)
    f.close()
    y = open(f"{output1Path}/{subject}/p{paperNumber}/numofpages.txt",'r+')
    y.write(finalPage)
    y.close()

def isBlankPage(currentPage):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage - 1]
    if page.extract_text().find("BLANK PAGE") == -1:
        return False
    return True

def getDimensions(currentPage, prevPixel):
    im = Image.open(f"{output1Path}/{subject}/p{paperNumber}/{currentPage}.jpg")
    pix = im.load()
    found = False
    i = 80
    while found == False:
        value = pix[147,prevPixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            if (prevPixel + i) > 2100:
                return ((prevPixel + i) - 30)
            else:
                i += 1
    return ((prevPixel + i) - 30)