import telebot;

bot = telebot.TeleBot('6927286954:AAEhRKHIw89Ajc9MAa1XJuy_EHd146qnpa4');
@bot.message_handler(commands=['start'])
def start_messege(start):
    bot.send_message(start.chat.id, 'Привет, Миша! Норм тему замутил? Напиши help')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
