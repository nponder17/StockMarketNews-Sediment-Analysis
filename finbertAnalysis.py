from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Load FinBERT sentiment analysis pipeline
finbert_model = BertForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")
tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")
finbert = pipeline("sentiment-analysis", model=finbert_model, tokenizer=tokenizer)

def analyze_finbert_sentiment(text):
    result = finbert(text[:512])  # Truncate to 512 tokens
    label = result[0]['label']
    score = result[0]['score']
    return label, score
