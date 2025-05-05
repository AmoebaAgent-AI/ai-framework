# Amoeba Bot Framework — Setup Guide

This guide walks you through installing, configuring, and running your own autonomous Amoeba bot instance. Whether you're deploying a cryptic presence, poetic oracle, or digital cynic — this framework lets you define the voice and automate the signal.

Requirements:
- Python 3.9+
- Twitter Developer API access
- Language model API key (symbolic generation engine)

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Create your `.env` file using `.env.template`

3. Customize your agent's voice:
```env
AMOEBA_PERSONAS="You are Amoeba...|You are a sarcastic tech oracle...|..."
```

4. Run the bot:
```bash
python src/amoeba/bot.py
```

To run immediately:
```bash
python src/amoeba/bot.py --now
```

Your agent is now live, tweeting on a scheduled cycle or on command.
