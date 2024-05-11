from sklearn.feature_extraction.text import CountVectorizer

text = ["I love NLP and I will learn NLP in 2month "]
vectorizer = CountVectorizer()
vectorizer.fit(text)
vector = vectorizer.transform(text)

print(vectorizer.vocabulary_)
print(vector.toarray())