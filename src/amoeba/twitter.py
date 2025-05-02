import tweepy
import os

client = tweepy.Client(
    consumer_key=os.getenv("X_CONSUMER_KEY"),
    consumer_secret=os.getenv("X_CONSUMER_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
)

def post_to_x(text):
    try:
        client.create_tweet(text=text)
        print("✅ Tweet posted")
    except Exception as e:
        print(f"❌ Error: {e}")
