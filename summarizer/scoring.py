def count_words(text):
    words = text.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq

def score_senteces(sentences, word_freq):
    scores = {}
    for sentence in sentences:
        words = sentence.split()

        if len(words) == 0:
            continue

        score = 0
        for word in words:
            if word in word_freq:
                score += word_freq[word]
        scores[sentence] = score / len(words)

    return scores