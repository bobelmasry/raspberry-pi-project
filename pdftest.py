from PyPDF2 import PdfReader



reader = PdfReader("example.pdf")
number_of_pages = reader.getNumPages()
page = reader.pages[20]
print(page.extract_text())
print(page.extract_text().find('9'))