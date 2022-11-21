import os
from httplib2 import Response
import tweepy
from dotenv import load_dotenv
load_dotenv()
import json


consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

def get_my_tweets(next_token=None):
    response = api.get_users_tweets(my_twitter_id, start_time=other_timestamp, end_time=now,max_results=100, pagination_token=next_token)
    for tweet in response.data:
        tweet_obj = {
            'id': tweet.id,
            'text': tweet.text
        }
        my_tweets.append(tweet_obj)
    if 'next_token' in str(response.meta):
        # print(response.meta['next_token'])
        get_my_tweets(response.meta['next_token'])


auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, return_type=Response)

my_twitter_id = input('What is your twitter id?  ')
other_timestamp = input('what do you want as your start time? (YYYY-MM-DDTHH:MM:SSZ) ') # EX: '2010-11-06T00:00:01Z' - this is the early timestamp in the search range
now = input('what do you want as your end time? (YYYY-MM-DDTHH:MM:SSZ) ') # EX: '2022-11-19T00:00:01Z'

my_tweets = []

get_my_tweets()
# print(len(my_tweets))


for tweet in my_tweets:
    url = f'https://twitter.com/tweets/status/{tweet["id"]}'
    print(url)
    tweet['url'] = url

with open('my_tweets.json','w') as f:
    f.write(json.dumps(my_tweets, indent=4))
    f.close()
