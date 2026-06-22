import cohere
from gensim.downloader import load
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

glove = load("glove-wiki-gigaword-50")

def enrich_prompt(prompt):
    words = word_tokenize(prompt.lower())
    words = [w for w in words if w not in stopwords.words('english')]

    enriched = prompt

    for word in words:
        try:
            similar = glove.most_similar(word, topn=2)
            enriched += " " + " ".join([w for w, _ in similar])
        except:
            pass

    return enriched

api_key = input("Enter API Key: ")
co = cohere.Client(api_key)

prompt = input("Enter Prompt: ")

enriched_prompt = enrich_prompt(prompt)

original_response = co.chat(
    model="command-a-03-2025",
    message=prompt
)

enriched_response = co.chat(
    model="command-a-03-2025",
    message=enriched_prompt
)

print("\n===== ORIGINAL PROMPT =====")
print(prompt)

print("\n===== ORIGINAL RESPONSE =====")
print(original_response.text)

print("\n===== ENRICHED PROMPT =====")
print(enriched_prompt)

print("\n===== ENRICHED RESPONSE =====")
print(enriched_response.text)

!pip install gensim cohere
