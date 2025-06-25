# Discord Greeting Bot 🤖

A simple and friendly Discord bot that responds to user greetings and gives time-based wishes.  
It also automatically joins or leaves a voice channel when the server owner connects or disconnects.

---

## 📌 Features

- Responds to basic greetings like: `hi`, `hello`, `hey`, etc.
- Sends appropriate messages based on the time of day:
  - Good Morning
  - Good Afternoon
  - Good Evening
  - Good Night
- Automatically joins or leaves voice channels based on a specific user's activity (server owner)

---

## ⚙️ Requirements

- Python 3.8 or above
- `discord.py` library

Install dependencies:

```bash
pip install -U discord.py
````

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/keishab06/discord-bot.git
cd discord-bot
```

### 2. Add Your Bot Token

Create a file named `token.txt` and paste your bot token inside:

```
your_discord_bot_token_here
```

> ⚠️ Do **NOT** share this token with anyone.

### 3. Configure Your Guild Owner ID

Create a file named `config.json` with the following content:

```json
{
  "GUILD_OWNER_ID": 123456789012345678
}
```

Replace the number with your actual Discord user ID.

### 4. Run the Bot

```bash
python discord_bot.py
```

---

## 📁 Project Structure

```
discord-greeting-bot/
├── discord_bot.py      # Main bot script
├── token.txt           # Your bot token (excluded from Git)
├── config.json         # Your Discord user ID (excluded from Git)
├── .gitignore          # Prevents sensitive files from being tracked
└── README.md           # Project overview and instructions
```

---

## 🛡️ Security Notes

* `token.txt` and `config.json` are **ignored via `.gitignore`**
* Do **not commit** sensitive files to GitHub

---

## 📄 License

This project is open-source and free to use or modify.

---

## 👤 Author

Made with ❤️ by Keisha
