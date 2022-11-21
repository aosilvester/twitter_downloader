# twitter_downloader
Twitter tweet downloader utilizing Python and Tweepy

## Description
supply a twitter id, start time, and end time and the twitter downloader will create a json list of all tweets inside the frame of time. Utilizes Python, Twitter, and Tweepy package.

## Requirements
python, a twitter account with developer access. you will need to setup the app in twitter. follow their developer docs for setting that up.

You need the following from twitter:
*  consumer_key, 
*  consumer_secret, 
*  access_token, 
*  access_token_secret

## Limitations:
It can only go back to about 2010(?) It also can only get so many tweets per request, so if you tweet prolificially for years, it will be better to do the search in smaller periods of time. I dont have the exact date or number limit, but its in tweepy's documentation. 