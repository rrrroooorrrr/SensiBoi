import tweepy
import os
from dotenv import load_dotenv
load_dotenv()
# Replace these placeholders with your Twitter API credentials
consumer_key        = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret     = os.getenv("TWITTER_CONSUMER_SECRET")
access_token        = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

sensi_bois = ['sensi boi',  'sensiboi']


# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.Client(bearer_token)

async def extract_search_criteria(message):
    # Split the message into words
    if message.content.startswith("how sensi are people about"):
        # Extract the topic from the message
        topic = message.content[len("how sensi are people about"):].strip()
    
        # # Initialize the search query and filters as empty strings
        search_query = ""
    
        # # Iterate through the words in the message
        # for word in words:
        #     # Check if the word is a search query or filter
        #     if word.startswith("#"):  # The word is a hashtag (part of the search query)
        #         search_query += word + " "
        #     elif word.startswith("-"):  # The word is a filter
        #         filters += word + " "
    
        # Strip any leading or trailing whitespace from the search query and filters
        search_query = topic
    
        return search_query

def search_tweets(search_query):
    # Search for tweets matching the search query
    tweets = api.search_recent_tweets(query=search_query, tweet_fields=['text'], user_fields = ['verified'], max_results=100)
    
    # Filter the tweets based on the specified filters
    # filtered_tweets = filter_tweets(tweets, filters)
    
    return tweets.data

# def filter_tweets(tweets, filters):
#     filtered_tweets = []
#     for tweet in tweets:
#         if tweet.user.verified:  # Check if the user who posted the tweet is verified
#             filtered_tweets.append(tweet)
#     return filtered_tweets
