import gensim.downloader as api
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load GloVe model
model = api.load("glove-wiki-gigaword-50")

# 10 Technology words
words = ["computer","internet","software","hardware","network",
         "data","server","database","programming","algorithm"]

# Get vectors
vectors = [model[w] for w in words]

# PCA
pca = PCA(n_components=2)
points = pca.fit_transform(vectors)

# Plot
for i, w in enumerate(words):
    plt.scatter(points[i,0], points[i,1])
    plt.text(points[i,0], points[i,1], w)

plt.title("Word Embeddings using PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()

# Similar words
print("\nTop 5 Similar Words to 'internet':")
print(model.most_similar("internet", topn=5))
