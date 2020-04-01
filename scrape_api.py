# Installing twitter module
# !pip install tweepy
import tweepy

# defining variables
# cosumer key
consumer_key="xxxxxxxxxxx"
consumer_sec="xxxxxxxxxxx"

# access details
access_key="xxxxxxxxxxxxxx"
access_sec="xxxxxxxxxxxxxx"

# lets connect at first step auth by using consumer access details

#dir(tweepy)
first_auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

# now setting second level of auth
first_auth.set_access_token(access_key,access_sec)

# pointing auth to data store
storage_api_connect=tweepy.API(first_auth,timeout=10)   # now after this step we can browse / search data from tweets
# to make it search it out for 10 sec, adding timeout

# now searching data as request and waiting for reply
# first method
# tweet_data=storage_api_connect.search('corona',count=30)
# print(tweet_data)

# second method
# search list what you want to search.
from textblob import TextBlob     # automated way of sentiment analysis
search_data=["facebook"]  # search list
list_of_tweets=[]    # tweet data store

#if len(search_data) >= 1:
if len(search_data) == 1:
  for tweetdata in tweepy.Cursor(storage_api_connect.search,q=search_data[0]+" -filter:retweets",lang='en',result_type='recent').items(100):
    list_of_tweets.append(tweetdata.text)
    analyse=TextBlob(tweetdata.text)
    print(analyse.sentiment)
    #print(analyse.sentiment.polarity)
    print(tweetdata.text)

print(list_of_tweets)

# using for loop
# for data in tweet_data:
#   print(data.text)
