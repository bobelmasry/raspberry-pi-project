from pdf2jpg import pdf2jpg
import os
i = 1
def output(inputPath, outputPath, pdfName):
    pdf2jpg.convert_pdf2jpg(inputPath, outputPath, dpi=250, pages="ALL")
    os.rename(f"C:/Users/donat/Documents/python_projects/output1/eco/p1/{pdfName}.pdf_dir",f"C:/Users/donat/Documents/python_projects/output1/eco/p1/{pdfName}")