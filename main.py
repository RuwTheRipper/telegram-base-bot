import os

import telebot

BOT_TOKEN = "TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, message.chat.id)

bot.infinity_polling()
