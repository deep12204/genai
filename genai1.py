from gensim.downloader import load
print("Loading pre-trained GloVe model(50 Dimensions)...")
model=load("glove-wiki-gigaword-50")
def ewr():
    result=model.most_similar(positive=['king','woman'],negative=['man'],topn=1)
    print("\n king-man+woman=?\n",result[0][0])
    print("\n similarity:",result[0][1])
    result=model.most_similar(positive=['paris','italy'],negative=['france'],topn=1)
    print("\nparis-france+italy=?",result[0][0])
    print("\n similarity:",result[0][1])
    result=model.most_similar(positive=['network'],topn=5)
    print("\nTop 5 words similar to networks are:\n")
    for word,similarity in result:
        print(word,similarity)
ewr()
