# sentiment_analysis.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize once
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Returns a sentiment label and score for a given text using VADER.
    Label is 'Positive', 'Neutral', or 'Negative'.
    """
    if not text.strip():
        return 'Neutral', 0.0  # handle empty strings safely

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        return 'Positive', compound
    elif compound <= -0.05:
        return 'Negative', compound
    else:
        return 'Neutral', compound
