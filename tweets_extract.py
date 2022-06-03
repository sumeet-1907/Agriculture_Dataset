import tweepy
import csv
import pandas as pd
import sys

# API credentials here
consumer_key = "Le1X93m9gqPt3JKyTZh41LGnj"
consumer_secret ="x8SG2tqdQgdbKvFysbVwdgMCGQ01pvIPec5jeGjuWJHbVO4sVp"
access_token= "767233969050050560-CC9ZWo3OOqkBHIGjdMICroiZ9prY7Ol"
access_token_secret ="msHCRiePw1Bthwg2F0fjFZOjpkkld98ktAEPlrKWl7TBR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

new_tweets = tweepy.Cursor(api.user_timeline, screen_name="EUAgri", tweet_mode='extended').items(500)

list = []
for tweet in new_tweets:
    text = tweet._json["full_text"]

    refined_tweet = {'text' : text,
                    'favorite_count' : tweet.favorite_count,
                    'retweet_count' : tweet.retweet_count,
                    'created_at' : tweet.created_at}
    
    list.append(refined_tweet)

df = pd.DataFrame(list)
df.to_csv('agri_tweets.csv')
