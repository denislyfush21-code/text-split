import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Пришли мне текст столбиком — я разобью его на отдельные сообщения.")

@bot.message_handler(func=lambda message: True)
def split_text(message):
    text = message.text
    if not text:
        return
    
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if line:  # пропускаем пустые строки
            bot.send_message(message.chat.id, line)

bot.infinity_polling()
