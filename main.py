import telebot

bot = telebot.TeleBot("1259998431:AAGd_n57AxjPUeuu-iU1cT9zgQyBZkDdGbY")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
