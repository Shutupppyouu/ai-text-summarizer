from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model = "facebook/bart-large-cnn"
)

def ai_summarize(text, max_length=50, min_length=30):
    summary = summarizer(
        text,
        max_length = max_length,
        min_length = min_length,
        do_sample = False
    )

    return summary[0]["summary_text"]