from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

corpus = [
    "Diabetes is a chronic disease that affects blood sugar",
    "Hypertension can lead to heart disease and stroke",
    "The patient was diagnosed with pneumonia and prescribed antibiotics",
    "Insulin therapy is commonly used for diabetes patients",
    "Cardiovascular diseases are the leading cause of death"
]

data = [s.lower().split() for s in corpus]

model = Word2Vec(data, vector_size=50, min_count=1)

print("Similar words to diabetes:")
print(model.wv.most_similar("diabetes"))

words = model.wv.index_to_key
vectors = [model.wv[w] for w in words]

points = PCA(n_components=2).fit_transform(vectors)

for i, w in enumerate(words):
    plt.scatter(points[i,0], points[i,1])
    plt.text(points[i,0], points[i,1], w)

plt.title("Medical Word Embeddings")
plt.show()
