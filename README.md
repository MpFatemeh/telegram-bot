# Telegram bots

2020 learning project: two small Python Telegram bots built with telepot.

- **calculator-telegram-bot.py**: asks for two numbers, then shows inline buttons for + - * / and replies with the result.
- **forwarder-telegram-bot.py**: forwards every document it receives to a Telegram channel.

## Run

```sh
pip install telepot
python calculator-telegram-bot.py
```

Set `TOKEN` (from BotFather) at the top of each script, and `CHANNEL` for the forwarder.
