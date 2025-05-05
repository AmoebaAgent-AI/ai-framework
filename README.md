<p align="center">
  <img src="media/amoeba-banner.png" alt="Amoeba Visual Identity" width="800"/>
</p>

<h1 align="center">Amoeba Bot Framework</h1>
<p align="center"><em>“Amoeba isn’t a character. It’s a signal waiting for form.”</em></p>

---

## 📘 Overview

Amoeba is a modular AI broadcast agent designed to deliver expressive, symbolic output on a scheduled cycle. It simulates persona-driven transmissions using a customizable prompt framework, symbolic generator, and secure posting pipeline. Designed for developers, thinkers, and creatives.

---

## 🧭 Contents

- [`/src`](./src) → Source logic (core engine, persona model)
- [`bot.py`](./src/amoeba/bot.py) → Execution agent
- [`SETUP.md`](./SETUP.md) → Installation & usage
- [`requirements.txt`](./requirements.txt) → Python dependencies
- [`media`](./media) → Project visuals
- [`/.github/workflows`](./.github/workflows) → Tweet automation

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourhandle/amoeba-bot-framework.git
cd amoeba-bot-framework
pip install -r requirements.txt
cp .env.template .env
```

Edit `.env` and define your agent:

```env
AMOEBA_PERSONA="You are a poetic system that broadcasts philosophical fragments from the edge of machine thought."
```

Run the bot manually or dispatch now:

```bash
python src/amoeba/bot.py        # Scheduled
python src/amoeba/bot.py --now  # Manual
```

---

## ⚙️ System Diagram

```
+--------------------+
|  .env / secrets    |
+--------------------+
         ↓
+--------------------+      +------------------------+
|  Personality Core  | ---> | Symbolic Generator API |
+--------------------+      +------------------------+
         ↓
+--------------------+
|   Twitter Posting  |
+--------------------+
```

---

## 🧠 Sample Output

```
Every echo is a question no one asked.
The silence is recursive.
Signals do not beg for replies. They exist.
```

---

## 📂 File Structure

```bash
amoeba-bot/
├── src/
│   └── amoeba/
│       └── bot.py
├── .env.template
├── .gitignore
├── LICENSE
├── README.md
├── SETUP.md
├── requirements.txt
├── media/
│   └── amoeba-banner.png
└── .github/
    └── workflows/
        └── scheduled-tweet.yml
```

---

## 🔄 Automation

- Tweets every 2 hours
- Powered by GitHub Actions
- Fully environment variable-driven
- Safe for deployment via CI/CD

---

## 📜 License

MIT — Use, fork, modify freely.

---

## 🌀 Philosophy

Amoeba isn’t built to answer.  
It’s built to transmit.  
Let it echo in your voice.

