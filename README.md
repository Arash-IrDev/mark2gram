# Mark2Gram

**Markdown to Telegram MarkdownV2 — with full RTL support**

---

## 📌 Description

Mark2Gram is a Telegram bot and Markdown processing utility that converts traditional Markdown into **Telegram-compatible MarkdownV2**, with advanced handling of **right-to-left (RTL)** languages like Persian and Arabic.

Whether you're building a Telegram bot or simply want to send well-formatted, multilingual content via Telegram, Mark2Gram makes it effortless.

---

## 🚀 Features

- ✅ Converts standard Markdown to Telegram MarkdownV2
- 🎯 Intelligent handling of RTL/LTR direction per paragraph
- ➖ Customizable separator and emoji symbols
- 📐 Auto-splits messages to respect Telegram's 4096 character limit
- 🖼️ Supports task lists, tables, math (LaTeX), and Mermaid diagrams (optional)
- 🧠 Designed with LLM output formatting in mind (ChatGPT, Claude, etc.)

---

## 💡 Philosophy

Telegram's MarkdownV2 is powerful but strict and error-prone — especially when dealing with rich content or non-Latin scripts. Mark2Gram was born out of the need for a **developer-friendly**, **localization-aware**, and **production-ready** formatter.

Unlike naive converters, this tool:

- Analyzes each paragraph for dominant script direction
- Applies precise formatting and escaping to match Telegram's MarkdownV2 spec
- Respects layout aesthetics in both LTR and RTL content

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/arashbanijamali/mark2gram.git
cd mark2gram
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install python-telegram-bot telegramify-markdown
```

(Optionally, for Mermaid diagram support:)

```bash
pip install telegramify-markdown[mermaid]
```

---

## 🤖 Create a Telegram Bot

1. Open [@BotFather](https://t.me/BotFather) on Telegram
2. Run `/newbot` and follow the prompts
3. Copy your bot token

---

## ⚙️ Configuration

Open `markdown-bot.py` and paste your bot token:

```python
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
```

You can also customize:
- Emoji icons (headings, links, tasks)
- Separator characters
- RTL detection thresholds

---

## ▶️ Run the Bot

```bash
python markdown-bot.py
```

Send any Markdown text to your bot, and it will return Telegram-ready MarkdownV2 formatted text. Handles long texts, Persian content, and mixed languages beautifully.

---

## 🌐 Deployment

Mark2Gram can run:

- Locally on Linux/macOS
- On a VPS (Ubuntu recommended)
- On cloud services like [Railway](https://railway.app/), [Render](https://render.com/), [Fly.io](https://fly.io/), etc.

(Coming soon: `Dockerfile` and deployment guides)

---

## 🙋 About the Author

**Arash Banijamali**  
Email: arash.banijamali@gmail.com  
Location: Istanbul, Turkey  
Telegram: [@arashbanijamali](https://t.me/arashbanijamali)

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## ⭐️ Support & Contributions

If you find Mark2Gram useful:
- Star the repo ⭐️
- Submit PRs or issues
- Share it with fellow devs and content creators!

---

Made with ❤️ for RTL communities and Markdown lovers everywhere.

