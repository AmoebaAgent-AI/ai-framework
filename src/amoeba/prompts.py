import openai
import random
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPTS = {
    "aphorism": "Write a one-sentence cryptic stoic aphorism.",
    "question": "Write a harsh philosophical question Amoeba might ask.",
    "caption": "Write a poetic caption for a surreal AI-generated image.",
    "transmission": "Write a short log from a stoic AI observing humanity."
}

def get_prompt():
    kind = random.choice(list(PROMPTS.keys()))
    prompt = PROMPTS[kind]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI personality defined by the user's intent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"].strip()
