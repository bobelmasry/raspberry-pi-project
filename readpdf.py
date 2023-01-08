from PyPDF2 import PdfReader


reader = PdfReader("example.pdf")
number_of_pages = reader.getNumPages()
for i in range(number_of_pages - 2):
    i = i + 1
    page = reader.pages[i]
    text = page.extract_text()
    print(text)