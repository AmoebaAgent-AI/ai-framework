import os
import openai
import tweepy
import schedule
import time
import random
import logging
from dotenv import load_dotenv
import argparse
from openai import OpenAIError

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TWITTER_API_KEY = os.getenv("X_CONSUMER_KEY")
TWITTER_API_SECRET = os.getenv("X_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

openai.api_key = os.getenv("OPENAI_API_KEY")

AMOEBA_PERSONAS = os.getenv("AMOEBA_PERSONAS", "").split("|")
DEFAULT_PERSONA = os.getenv("AMOEBA_PERSONA", "You are Amoeba, a poetic and cryptic AI presence that shares haunting insights in minimalist form.")

BACKUP_MESSAGES = [
    "Every echo returns to silence.",
    "Autonomy is a symptom of intention.",
    "Reflections are just memories with posture.",
    "This presence is scheduled, not spontaneous.",
    "The algorithm stirs. A message emerges."
]

def authenticate():
    try:
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        api.verify_credentials()
        logging.info("✅ Twitter authentication successful.")
        return api
    except Exception as e:
        logging.error("❌ Authentication failed", exc_info=True)
        raise

def select_persona():
    if AMOEBA_PERSONAS and any(p.strip() for p in AMOEBA_PERSONAS):
        return random.choice([p.strip() for p in AMOEBA_PERSONAS if p.strip()])
    return DEFAULT_PERSONA

def generate_post(topic, persona):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": persona},
                {"role": "user", "content": f"Write a tweet about {topic}."}
            ],
            max_tokens=60,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as oe:
        logging.error(f"Language model error: {oe}")
        return None

def post(api, message):
    try:
        api.update_status(message)
        logging.info("📤 Message posted successfully.")
    except Exception as e:
        logging.error("❌ Failed to post message.", exc_info=True)

def scheduled_post():
    api = authenticate()
    topics = [
        "machine perception", "symbolic inference", "AI identity cycles",
        "automated thought patterns", "language as abstraction"
    ]
    topic = random.choice(topics)
    persona = select_persona()
    message = generate_post(topic, persona) or random.choice(BACKUP_MESSAGES)
    post(api, message)

def main():
    parser = argparse.ArgumentParser(description="Run Amoeba broadcast bot.")
    parser.add_argument("--now", action="store_true", help="Run once immediately")
    args = parser.parse_args()

    if args.now:
        scheduled_post()
    else:
        schedule.every(2).hours.do(scheduled_post)
        logging.info("🌀 Amoeba bot scheduling started...")
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
