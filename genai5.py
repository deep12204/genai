from gensim.downloader import load
import cohere
model = load("glove-wiki-gigaword-50")
co = cohere.Client(input("API Key: "))
seed = input("Enter seed word: ")
words = [w for w, _ in model.most_similar(seed, topn=10)]
prompt = f"Write a paragraph about {seed} using: {', '.join(words)} Write in 5-6 sentences with proper line breaks."
response = co.chat(
    model="command-a-03-2025",
    message=prompt
)
print("\nSimilar Words:")
print(words)
print("\nGenerated Paragraph:")
print(response.text)
