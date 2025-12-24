def input_lines():
    print("Enter text here: ")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return " ".join(lines)

def plain_text(text):
    text = text.lower()
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("!","")
    text = text.replace("?","")
    return text

def split_into_sentences(text):
    #split text into sentences using periods
    sentences = text.split(".")
    #Remove empty sentences and remove whitespace
    sentences = [s.strip() for s in sentences if s.strip() != ""]
    return sentences

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
        score = 0
        for word in words:
            if word in word_freq:
                score += word_freq[word]
        scores[sentence] = score

    return scores


def main():
    text = input_lines()
    sentences = split_into_sentences(text)
    clean_sentences = []
    for sentence in sentences:
        clean_sentences.append(plain_text(sentence))
    
    clean_text = " ".join(clean_sentences)

    word_freq = count_words(clean_text)
    sentence_scores = score_senteces(clean_sentences, word_freq)
    
    print("\nSentence Scores")
    for sentence, score in sentence_scores.items():
        print(f"{sentence} -> {score}")


if __name__ == "__main__":
    main()