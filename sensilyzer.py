import nltk
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import statistics

def median(numbers):
    return statistics.median(numbers)



def analyze_tweet_sentiments(tweets):
  nltk_sentiments = []
  textblob_sentiments = []
  vader_sentiments = []

  # Initialize the sentiment analyzers
  nltk_sentiment_analyzer = nltk.sentiment.vader.SentimentIntensityAnalyzer()
  vader_sentiment_analyzer = SentimentIntensityAnalyzer()

  # Analyze the sentiment of each tweet using the different libraries
  for tweet in tweets:
    tweetText = tweet.text
    textblob_sentiment_analyzer = TextBlob(tweetText) 
      
    nltk_sentiments.append(nltk_sentiment_analyzer.polarity_scores(tweetText))
    textblob_sentiments.append(textblob_sentiment_analyzer.sentiment.polarity)
    vader_sentiments.append(vader_sentiment_analyzer.polarity_scores(tweetText))

  # Combine the scores from the different libraries
  combined_sentiments = []
  for i in range(len(tweets)):
    combined_sentiments.append((nltk_sentiments[i]['compound'] + textblob_sentiments[i] + vader_sentiments[i]['compound']) / 3)

  # Calculate the median sentiment
  median_sentiment = median(combined_sentiments)

  # Calculate the average sentiment
  average_sentiment = sum(combined_sentiments) / len(combined_sentiments)
  combined_sentiments_sum = sum(combined_sentiments)

  return combined_sentiments, combined_sentiments_sum, median_sentiment, average_sentiment
