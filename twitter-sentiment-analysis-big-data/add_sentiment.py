import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


df = pd.read_csv('/home/elifnehirozer/Downloads/cleaned_tweets.csv')


analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    if pd.isnull(text):
        return 'neutral'
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'


df['sentiment'] = df['text'].apply(get_sentiment)


df.to_csv('/home/elifnehirozer/Downloads/tweets_with_sentiment.csv', index=False)

print("Sentiment column added. New File: tweets_with_sentiment.csv")
