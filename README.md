# GPT Adventure — Interactive Story Builder

GPT Adventure is a terminal-based Python application that uses OpenAI's GPT-3.5 API to create interactive, user-driven stories. The user selects a language and genre, then engages in a text-based adventure where GPT plays the role of a wise and immersive storyteller.

---

## 📦 Features

- Language selector (English, Korean, etc.)
- Genre selector (Fantasy, Sci-Fi, Horror...)
- Narrator-style GPT storytelling using Chat API
- Chapter system: pauses every 10 turns for story pacing
- Commands: `/help`, `/save`, `/restart`, `/quit`
- Story log saved to `story_log.txt` after each exchange
- API key loaded securely from environment variable

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Software-Engineering-8-8-8-8-Squad/12220266.git
cd 12220266
```

2. **Install the required package**
```bash
pip install openai
```

3. **Set your API key (temporary):**
```bash
export OPENAI_API_KEY="OPENAI_API_KEY"
```

4. **Run the program**
```bash
python3 gpt_adventure.py
```

---

## 📁 Files Included

- `gpt_adventure.py` – main application script
- `story_log.txt` – optional story output file (auto-generated)
- `README.md` – this file

---

## 💡 Inspired By

Lab 4.9.2 (REST API integration) from the Cisco Software Engineering curriculum — adapted to GPT for creative interaction.
