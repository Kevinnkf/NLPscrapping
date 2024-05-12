import PyPDF2
import re
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

text = ""

# Function to extract text from PDF
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

# Function to classify the text based on pasal
def classifyPasal(text):
    # Split the text into sections based on occurrences
    sections = re.split(r'pasal \d+', text, flags=re.IGNORECASE)
    
    # Filter out empty sections
    sections = [section.strip() for section in sections if section.strip()]
    
    for i in range(1, len(sections)):
        sections[i] = "Pasal " + re.search(r'\d+', sections[i-1], flags=re.IGNORECASE).group() + sections[i]

    return sections

# Function to find all typos
def correctedTypos(text):
    df = pd.DataFrame({'Peraturan': text})
    top5 = df.head()
    df['Peraturan'] = top5['Peraturan'].apply(lambda x: str(TextBlob(x).correct()))
    return df

# Function to find all common words
def removeStopWords():
    df = pd.DataFrame({'Peraturan': text})
    stop = stopwords.words('indonesia')
    df['Peraturan'] = df['Peraturan'].apply(lambda x: "".join(x for x in x.split() if x not in stop))






# Calling the extract text function
pdf_text = extract_text_from_pdf("C:/Users/khalf/Code/NLP/Undang-Undang Nomor 1 Tahun 20230.pdf", exclude_patterns=["Presiden Republik Indonesia", "SK No 16003 A"])

# Classifying all the text based on pasal
classified_text = classifyPasal(pdf_text)

# Correct typos in classified text
corrected_text_df = correctedTypos(classified_text)

#for index, row in corrected_text_df.iterrows():
#   print(row['Peraturan'])

print(corrected_text_df.shape)