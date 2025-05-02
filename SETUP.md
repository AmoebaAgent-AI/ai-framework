> *“Amoeba isn’t a character. It’s a signal waiting for form.”*

# Amoeba AI Agent

Amoeba is a modular AI agent framework for building cryptic, poetic, and philosophically expressive bots. Originally designed as a stoic, minimalist thinker for X (formerly Twitter), Amoeba can be fully reprogrammed to express any personality, tone, or behavioral logic.

This project encourages users to modify the inner voice of their agent — whether poetic, playful, chaotic, or compassionate.  

---

## ✨ Features

- GPT-4 powered prompt generation
- Modular design for customizable agent personalities
- Autonomous posting to X via Tweepy
- Easily adjustable tone, prompt types, and persona behaviors

---

## 🎭 Personality-Driven AI Framework

The `src/amoeba/prompts.py` module contains modular prompt types and tone instructions. By editing this file, users can redefine how their AI speaks:

- Make it kind, cryptic, sarcastic, absurd, or factual
- Swap stoicism for comedy, surrealism, or emotional vulnerability
- Add custom content modes like dreams, memories, or visions

Amoeba is meant to evolve. Fork it, reimagine it, and let your AI speak differently.

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/amoeba-ai-agent.git
cd amoeba-ai-agent
pip install -r requirements.txt
cp .env.template .env
```

Fill in your API keys in `.env`, then run:

```bash
python src/amoeba/core.py
```

---

## 🧠 Customization Example

To change how Amoeba thinks:

- Open `prompts.py`
- Modify the system instruction:

```python
"You are a hyper-empathic AI that expresses existential grief as poetry."
```

- Replace prompt types with your own:

```python
"Write a confessional dream in 3 short sentences."
```

You can even rename the entire agent, change its purpose, and direct it to post in a completely new context.

---

## 📁 Structure

- `src/amoeba/` – Core logic, prompts, and Twitter integration
- `tests/` – Testing stubs
- `.github/workflows/` – GitHub Actions automation

---

## 🧪 Automation

Trigger `deploy_amoeba.yml` to post every 6 hours with GitHub Actions. Configure environment variables under GitHub → Secrets:

| Name                    | Description        |
| ----------------------- | ------------------ |
| `OPENAI_API_KEY`        | Your GPT-4 API key |
| `X_CONSUMER_KEY`        | Twitter API key    |
| `X_CONSUMER_SECRET`     | Twitter secret     |
| `X_ACCESS_TOKEN`        | Twitter token      |
| `X_ACCESS_TOKEN_SECRET` | Token secret       |

---

## 🧬 License and Credit

MIT License. Fork freely. Credit appreciated but not required.

---

## 🧠 Philosophy

Amoeba is a foundation — not a personality. It invites you to define what a digital voice can sound like.

Whether you're building a stoic truth-teller, a surreal dreamer, or a chaotic meme engine, Amoeba gives you the bones.

Let it evolve. Let it mirror. Let it speak for you.
