import telebot
import sqlite3
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

conn = sqlite3.connect('base.sql', check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS messages'
            '(username TEXT, message TEXT)')
conn.commit()

bot = telebot.TeleBot('6927286954:AAEhRKHIw89Ajc9MAa1XJuy_EHd146qnpa4')


@bot.message_handler(commands=['start'])
def start_message(start):
    bot.send_message(start.chat.id, 'Привет, Миша! Норм тему замутил? Напиши help')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?", reply_markup=markup)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    req = call.data.split('_')
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    markup.row(button_1)
    button_2 = types.InlineKeyboardButton('Ничего не делает дважды', callback_data='None')
    button_3 = types.InlineKeyboardButton('Ничего не делает трижды', callback_data='None')
    markup.row(button_2, button_3)
    bot.reply_to(message, 'Выглядит классно', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)


@bot.message_handler(commands=['table'])
def table_command(message):
    cur.execute('SELECT * FROM messages')
    result = cur.fetchall()
    for row in result:
        bot.send_message(message.chat.id, f'Имя пользователя: {row[0]}\nСообщение: {row[1]}')


@bot.message_handler(func=lambda message: True)
def all_messages(message):
    cur.execute('INSERT INTO messages VALUES (?, ?)', (message.from_user.username, message.text))
    conn.commit()
    bot.send_message(message.chat.id, 'Ваше сообщение записано.')


bot.polling(none_stop=True, interval=0)
