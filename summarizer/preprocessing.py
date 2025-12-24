STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while",
    "is", "are", "was", "were", "be", "been", "being",
    "to", "of", "in", "on", "for", "with", "as", "by",
    "at", "from", "that", "this", "it", "its"
}

def preprocess_text(text):
    text = text.lower()
    
    punctuation = ".,!?;:"
    for char in punctuation:
        text = text.replace(char, "")
    
    words = text.split()

    filtered_words = []
    for word in words:
        if word not in STOP_WORDS:
            filtered_words.append(word)

    return " ".join(filtered_words)