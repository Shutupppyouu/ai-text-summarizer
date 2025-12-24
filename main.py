from summarizer.preprocessing import preprocess_text
from summarizer.scoring import count_words, score_senteces
from summarizer.extractive import select_top_sentences

def input_lines():
    print("Enter text here: ")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return " ".join(lines)

def split_into_sentences(text):
    #split text into sentences using periods
    sentences = text.split(".")
    #Remove empty sentences and remove whitespace
    sentences = [s.strip() for s in sentences if s.strip() != ""]
    return sentences

def main():
    text = input_lines()
    sentences = split_into_sentences(text)
    clean_sentences = []
    for sentence in sentences:
        clean_sentences.append(preprocess_text(sentence))
    
    clean_text = " ".join(clean_sentences)

    word_freq = count_words(clean_text)
    sentence_scores = score_senteces(clean_sentences, word_freq)
    
    summary = select_top_sentences(sentence_scores, sentences, n=2)

    print("\nSummary:")
    for s in summary:
        print(s)


if __name__ == "__main__":
    main()