import PyPDF2
import re
import pandas as pd
from textblob import TextBlob
from textblob import Word
import nltk
from nltk.corpus import stopwords
import pandas as pd
import spacy
import spacy_stanza

# nlp = spacy_stanza.load_pipeline("id")  # Load the model
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
    # Split the text into sections based on occurrences of "pasal"
    sections = re.split(r'(\bPasal \d+\b)', text, flags=re.IGNORECASE)
    
    # Initialize lists to hold "Pasal" and "isi"
    pasals = []
    contents = []
    
    # Iterate through the sections and classify them
    for i in range(1, len(sections), 2):
        pasal = sections[i].strip()  # Get the "Pasal"
        isi = sections[i + 1].strip() if (i + 1) < len(sections) else ''  # Get the content
        pasals.append(pasal)
        contents.append(isi)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'pasal': pasals,
        'isi': contents
    })

    # Apply transformations
    df['pasal'] = df['pasal'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    df['isi'] = df['isi'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    
    return df

    
    

# def classify_Bab(text):
#     # Create a DataFrame

#     # penjara = 
#     # tutupan = 
#     # denda = 
#     # pengawasan = 
#     # kerja_sosial = 


#     df = pd.DataFrame({
#         'Penjara': penjara,
#         'Tutupan': tutupan,
#         'Denda': denda,
#         'Pengawasan': pengawasan,
#         'Kerja_Sosial': kerja_sosial
#         })
#     })

# Function to find all typos
def correctedTypos(text):
    df = pd.DataFrame({'Peraturan': text})
    top5 = df.head()
    df['Peraturan'] = top5['Peraturan'].apply(lambda x: str(TextBlob(x).correct()))
    return df

# Function to find all common words
def removeStopWords(text):
    df = pd.DataFrame({'Peraturan': text})
    stop = stopwords.words('indonesia')
    df['Peraturan'] = df['Peraturan'].apply(lambda x: "".join(x for x in x.split() if x not in stop))
    return df['Peraturan']

# Function to lemmatize words
def lemmatization(text):
    df = pd.DataFrame({'Peraturan': text})
    df['Peraturan'] = df['Peraturan'].apply(lambda x: " ".join([token.lemma_ for token in nlp(x)]))
    return df['Peraturan']

# # lowercasing
# def lowercasing(text):
#     df = pd.DataFrame({
#         'pasal': pasals,
#         'isi': contents
#     })
#     df['pasal'] = df['pasal'].apply(lambda x: "".join(x.lower() for x in x.split()))
#     return df['pasal']


# Calling the extract text function
pdf_text = extract_text_from_pdf("C:/Users/khalf/Code/NLP/draft_ruu_kuhp_final.pdf", "")
# ?print(pdf_text)

# Classifying all the text based on pasal
classified_text = classifyPasal(pdf_text)
print(classified_text.head)