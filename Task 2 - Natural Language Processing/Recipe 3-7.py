import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

sentences = [['I', 'love', 'nlp'],
 ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
 ['nlp', 'is', 'future'],
 ['nlp', 'saves', 'time', 'and', 'solves',
 'lot', 'of', 'industry', 'problems'],
 ['nlp', 'uses', 'machine', 'learning']]

# training the model
skipgram = Word2Vec(sentences, vector_size =50, window = 3, min_count=1,
sg = 1)
print(skipgram)
    
# access vector for one word
print(skipgram.wv['nlp'])

# save model
skipgram.save('skipgram.bin')

# load model
skipgram = Word2Vec.load('skipgram.bin')

# T-SNE plot
X = skipgram.wv.vectors
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])

# access the vocabulary using key_to_index and index_to_key
index_to_key = skipgram.wv.index_to_key
for i, word_index in enumerate(index_to_key):
    word = index_to_key[i]
pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()