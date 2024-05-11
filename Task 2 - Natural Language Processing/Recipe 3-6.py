#Import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

Text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]

#Create the transform
vectorizer = TfidfVectorizer()

#Tokenize and build vocab
vectorizer.fit(Text)

 # Summarize
print("Vocabulary:")
print(vectorizer.vocabulary_)
print("\nIDF Scores:")
print(vectorizer.idf_)

# Transform the text data into TF-IDF features
X = vectorizer.transform(Text)

# Convert the sparse matrix to a dense array for better visualization
X_dense = X.toarray()

 # Get feature names
feature_names = vectorizer.get_feature_names_out()

 # Create DataFrame for better visualization
tfidf_df = pd.DataFrame(X_dense, columns=feature_names)
        
print("\nTF-IDF Features:")
print(tfidf_df)