import os
import discord
import tweeter
import statistics
from textblob import TextBlob
from nltk import download
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dotenv import load_dotenv

download('vader_lexicon')
env_loaded = load_dotenv()

discord_bot_token   = os.getenv("DISCORD_BOT_TOKEN")
my_server           = int(os.getenv("SELF_SERVER"))
my_channel          = int(os.getenv("SELF_GENERAL_CHANNEL"))


def median(numbers):
    return statistics.median(numbers)


intents                 = discord.Intents.default()
intents.message_content = True
intents.messages        = True
intents.guilds          = True
client                  = discord.Client(intents=intents)


@client.event
async def on_ready():
    channel = client.get_channel(my_channel)  # Replace <channel_id> with the ID of the channel
    await channel.send("Hey Zaddy, I'm sensi rn.")


@client.event
async def on_message(message):
    # Only process messages that are not from the bot itself
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    if 'sensi boi' in message.content.lower() or 'sensiboi' in message.content.lower():
        await message.channel.send('Somebody Sensi RN??')
    
    # Extract the topic from the message
    searchCriteria = await tweeter.extract_search_criteria(message)
    await tweeter.extract_search_criteria(message)
    if searchCriteria:
        tweets = tweeter.search_tweets(searchCriteria)
    
    # Analyze the sentiment of the tweets using TextBlob and NLTK
    # Combine the scores from TextBlob and NLTK to compute a final sentiment score
        final_sentiment = [compute_final_sentiment(tweet) for tweet in tweets]
    
    # get median and average
        median_score = median(final_sentiment)
    
        average_score = sum(final_sentiment) / len(final_sentiment)
        if median_score < 0:
            language = "negative"
            await message.reply(f"{searchCriteria} has a {language} score, probably because it sucks. The median sentiment is {median_score} and the average is {average_score}")
        elif median_score > 0:
            language = "positive"
            await message.reply(f"{searchCriteria} has a {language} score, probably because it's good or people are stupid. The median sentiment is {median_score} and the average is {average_score}")
        else:
            language = "neutral"
            await message.reply(f"{searchCriteria} has a {language} score, probably because it's uninteresting or people have better things to do. The median sentiment is {median_score} and the average is {average_score}")

    

def compute_final_sentiment(tweet):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    
    textblob_sentiment = TextBlob(tweet.text).sentiment
    nltk_sentiment = sentiment_analyzer.polarity_scores(tweet.text)
        
    # Combine the polarity and subjectivity scores from TextBlob
    textblob_score = textblob_sentiment.polarity * textblob_sentiment.subjectivity
    
    # Combine the positivity, negativity, and neutrality scores from NLTK
    nltk_score = nltk_sentiment['pos'] - nltk_sentiment['neg'] - nltk_sentiment['neu']
    
    # Return the average of the scores from TextBlob and NLTK as the final sentiment score
    final_score = (textblob_score + nltk_score) / 2
    return final_score



client.run(discord_bot_token)
