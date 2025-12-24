from .preprocessing import preprocess_text

def select_top_sentences(sentence_scores, original_sentences, n = 2):
    #sort sentences by score (high to low)
    sorted_sentences = sorted(
        sentence_scores.items(),
        key = lambda item: item[1],
        reverse = True
    )

    #select top N sentences
    top_sentences = [sentence for sentence, score in sorted_sentences[:n]]

    #preserve the original order
    ordered_summary = []
    for sentence in original_sentences:
        clean_sentence = preprocess_text(sentence)
        if clean_sentence in top_sentences:
            ordered_summary.append(sentence)

    return ordered_summary