import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from secret import API_KEY
from context import *

bot = telebot.TeleBot(API_KEY, parse_mode=None)

create_database()

data = {}

# data['124234'] = {
#     "model": None,
#     "year": None,
#     "color": None
# }
# data['323433'] = {}

# data['124234']["username"] = "Khayriddin"

@bot.message_handler(commands=['start', 'help'])
def say_hello(message):
    data[message.chat.id] = {
        "model": None,
        "prod_year": None,
        "color": None
    }
    is_user_exist = get_user(message.chat.id)
    if is_user_exist == False:
        add_user(message.chat)
    btn1 = InlineKeyboardButton("start")
    btn2 = KeyboardButton("help")
    btn3 = KeyboardButton("menu")
    # btn4 = KeyboardButton("exit")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, "Welcome to my bot", reply_markup=markup)

main_command = None

@bot.message_handler()
def handler(message):
    global main_command
    global data
    print(data)
    if message.text == "start" or main_command == 'start':
        main_command = "start"
        if message.text == "start":
            bot.send_message(message.chat.id, f"Enter cars model: ")
        elif data[message.chat.id]['model'] == None:
            data[message.chat.id]['model'] = message.text
            bot.send_message(message.chat.id, f"Enter cars prod_year: ")
        elif data[message.chat.id]['prod_year'] == None:
            data[message.chat.id]['prod_year'] = message.text
            bot.send_message(message.chat.id, f"Enter cars color: ")
        elif data[message.chat.id]['color'] == None:
            data[message.chat.id]['color']=message.text
            main_command = None
            bot.send_message(message.chat.id, f"Car object added succesifully!")
    else:
        bot.send_message(message.chat.id, "Else")


bot.infinity_polling()