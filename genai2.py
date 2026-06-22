import gensim.downloader as api
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model = api.load("glove-wiki-gigaword-50")

words = ["computer","internet","software","hardware","network",
         "data","server","database","programming","algorithm"]

vectors = [model[w] for w in words]

pca = PCA(n_components=2)
points = pca.fit_transform(vectors)

for i, w in enumerate(words):
    plt.scatter(points[i,0], points[i,1])
    plt.text(points[i,0], points[i,1], w)

plt.title("Word Embeddings using PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()

print("\nTop 5 Similar Words to 'internet':")
print(model.most_similar("internet", topn=5))
