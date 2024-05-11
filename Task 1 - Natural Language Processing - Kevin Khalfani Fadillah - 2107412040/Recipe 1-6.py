import re
import requests

# Tokenizing
#run the split query
print(re.split(r'\s+', 'I like this book.'))

# Extracing email IDs
#Read/create the document or sentences
doc = "For more details please mail us at: xyz@abc.com,pqr@mno.com"
#Execute the re.findall function
addresses = re.findall(r'[\w.-]+@[\w.-]+', doc)
for address in addresses:
    print(address)

# Extracing email IDs
#Read/create the document or sentences
doc = "For more details please mail us at xyz@abc.com"
#Execute the re.sub function
new_email_address = re.sub(r'([\w.-]+)@([\w.-]+)',
                           r'pqr@mno.com', doc)
print(new_email_address)

# Define the URL of the book
url = 'https://www.gutenberg.org/files/2638/2638-0.txt'


# Define a function to extract the content from the book
def get_book(url):
    #Sends a HTTP request to get    the text from Project Gutenberg
    raw = requests.get(url).text
    #Find the start and end of the book content using more flexible patterns
    start_match = re.search(r"\*\*\* START OF (?:THIS|THE) PROJECT GUTENBERG EBOOK .* \*\*\*", raw)
    end_match = re.search(r"\*\*\* END OF (?:THIS|THE) PROJECT GUTENBERG EBOOK .* \*\*\*", raw)
    #Check if both start and end matches are found
    if start_match and end_match:
        start = start_match.end()
        stop = end_match.start()
        #Keeps the relevant text
        text = raw[start:stop]
        return text
    else:
        print("Failed to extract book content. Start or end marker not found.")
        return None

# Define a function to preprocess the text data
def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+', ' ', sentence).lower()

# Call the get_book function to extract the book content
book = get_book(url)

# Preprocess the extracted book content
processed_book = preprocess(book)

# Print the preprocessed book content
print(processed_book)

# Count number of times "the" is appeared in the book
len(re.findall(r'the', processed_book))

# Replace "i" with "I"
processed_book = re.sub(r'\si\s', " I ", processed_book)
print(processed_book)

# find all occurance of text in the format "abc--xyz"
occurance = re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book)
print (occurance)
