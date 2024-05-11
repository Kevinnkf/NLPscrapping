from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

Text = "I am learning NLP"
TextBlob(Text).ngrams(1)
TextBlob(Text).ngrams(2)

# Text
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer(ngram_range=(2,2))
# tokenizing
vectorizer.fit(text)
# encode document
vector = vectorizer.transform(text)
# summarize & generating output
print(vectorizer.vocabulary_)
print(vector.toarray())
