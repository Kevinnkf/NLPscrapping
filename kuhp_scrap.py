import PyPDF2
import re

text = ""

def extract_text_from_pdf(pdf_path, exclude_patterns = None):
    text = ""
    if exclude_patterns is None:
        exclude_patterns = []

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()

            # Exclude specified patterns from the extracted text
            for pattern in exclude_patterns:
                page_text = page_text.replace(pattern, '')

            text += page_text
    return text

def classifyPasal(text):
    # Split the text into sections based on occurrences
    sections = re.split(r'pasal \d+', text, flags=re.IGNORECASE)
    
    # Filter out empty sections
    sections = [section.strip() for section in sections if section.strip()]
    
    for i in range(1, len(sections)):
        sections[i] = "Pasal " + re.search(r'\d+', sections[i-1], flags=re.IGNORECASE).group() + sections[i]

    return sections

pdf_text = extract_text_from_pdf("C:/Users/khalf/Code/NLP/Undang-Undang Nomor 1 Tahun 20230.pdf", exclude_patterns=["Presiden Republik Indonesia", "SK No 16003 A"])
classified_text = classifyPasal(pdf_text)
for section in classified_text:
    print(section)
    print("------------")