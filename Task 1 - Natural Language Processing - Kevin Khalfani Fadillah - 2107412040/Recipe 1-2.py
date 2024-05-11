import PyPDF2
from PyPDF2 import PdfReader

#Creating a pdf file object
pdf = open("file.pdf", "rb")

#creating pdf reader object
pdf_reader = PyPDF2.PdfReader(pdf)

#checking number of pages in a pdf file
num_pages = len(pdf_reader.pages)
print(num_pages)

#creating a page object
first_page = pdf_reader.pages[0]

#finally extracting text from the page
text = first_page.extract_text()
print (text)    
