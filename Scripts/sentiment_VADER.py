import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def compute_sentiment_VADER(tokens):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = np.mean([analyzer.polarity_scores(sentence)['compound'] for sentence in tokens])
    return sentiment