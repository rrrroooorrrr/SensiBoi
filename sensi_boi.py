import os
import discord
import tweeter
import sensilyzer
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
        combined_sentiments, combined_sentiments_sum, median_sentiment, average_sentiment = sensilyzer.analyze_tweet_sentiments(tweets)
    
    # get median and average

        if median_sentiment < 0:
            language = "negative"
            await message.reply(f"{searchCriteria} has a {language} combined score of {combined_sentiments_sum}, probably because it sucks. The median sentiment is {median_sentiment} and the average is {average_sentiment}")
        elif median_sentiment > 0:
            language = "positive"
            await message.reply(f"{searchCriteria} has a {language} combined score of {combined_sentiments_sum}, probably because it's good or people are stupid. The median sentiment is {median_sentiment} and the average is {average_sentiment}")
        else:
            language = "neutral"
            await message.reply(f"{searchCriteria} has a {language} combined score of {combined_sentiments_sum}, probably because it's uninteresting or people have better things to do. The median sentiment is {median_sentiment} and the average is {average_sentiment}")




client.run(discord_bot_token)
