import tweepy
from credentials import * 
  
def on_tweet(tweet):
    print(f"{tweet.id}")
    #print(f"{tweet.text}")
    print("-"*50)
    words = (tweet.text).split()
    for word in words:
        print(word)
    print("-"*50)



client = tweepy.Client(bearer_token=bearer)

# Replace with your own search query
response = client.search_recent_tweets('@Brianmsk_ 13745',max_results=15)

tweets = response.data

for tweet in tweets:
    on_tweet(tweet)


