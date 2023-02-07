from PyPDF2 import PdfReader 
from PIL import Image
import tools

subject = 'eco'
subjectCode = '9708'
paperNumber = 1
pdfPath = r"C:\Users\donat\Documents\python_projects\Teachmegcse\teachmegcse3\Teachmegcse1\past_papers\static\past_papers\9708\9708_m16_qp_12.pdf"
output1Path = r"C:\Users\donat\Documents\python_projects\output1"
currentQuestion = 1
numOfQuestionsInPage = 0
numOfQuestions = 30
reader = PdfReader(pdfPath)
initialQuestion = tools.getInitial()[0]
initialPage = tools.getInitial()[1]

tools.makeImages()
numberOfPages = reader.getNumPages()
i = 2
for i in range(numberOfPages - 1):
    if tools.isBlankPage(i) == True:
        i += 1  
    else:
        numOfQuestionsInPage = tools.numOfQuestionsInPage(i, currentQuestion)
        firstQuestionInPage = True
        for j in range(numOfQuestionsInPage):
            if firstQuestionInPage:
                startY = 150
                endY = tools.getDimensions(i, startY)
                nextY = tools.getDimensions(i, startY)
                tools.takeScreenshot(startY, endY, currentQuestion, i, subjectCode)
                firstQuestionInPage = False
                currentQuestion += 1
            elif j == numOfQuestionsInPage:
                startY = nextY
                endY = 2100
                tools.takeScreenshot(startY, endY, currentQuestion, i, subjectCode)
                i += 1
                currentQuestion += 1
            else:
                startY = nextY
                endY = tools.getDimensions(i, startY)
                nextY = tools.getDimensions(i, startY)
                tools.takeScreenshot(startY, endY, currentQuestion, i, subjectCode)
                currentQuestion += 1

finalQuestion = int(initialQuestion) + numOfQuestions
finalQuestion = str(finalQuestion) 
finalPage = int(initialPage) + numberOfPages
finalPage = str(finalPage)
tools.saveFinal(finalQuestion, finalPage)
