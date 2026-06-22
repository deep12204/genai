import spacy
nlp = spacy.load("en_core_web_sm")
IPC = {
    "302": "Section 302 IPC: Punishment for murder.",
    "375": "Section 375 IPC: Definition of rape.",
    "420": "Section 420 IPC: Cheating and fraud.",
    "376": "Section 376 IPC: Punishment for rape.",
    "124a": "Section 124A IPC: Sedition."
}
def get_section(text):
    doc = nlp(text)
    for token in doc:
        if token.text.lower() in IPC:
            return token.text.lower()
    return None
print("IPC Chatbot Started")
while True:
    user = input("You: ")
    if user.lower() in ["exit", "bye"]:
        print("Bot: Goodbye!")
        break
    elif user.lower() in["hi","hello"]:
        print("Bot: Hello! Ask me about IPC sections.")
    else:
        section = get_section(user)
        if section:
            print("Bot:", IPC[section])
        else:
            print("Bot: Ask about IPC sections like 302 or 420.")

