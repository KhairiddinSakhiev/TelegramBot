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
    btn1 = InlineKeyboardButton("add")
    btn2 = KeyboardButton("get-all")
    btn3 = KeyboardButton("get")
    btn4 = KeyboardButton("update")
    btn5 = KeyboardButton("delete")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(message.chat.id, "Welcome to my bot", reply_markup=markup)

main_command = None
idupdate = None
@bot.message_handler()
def handler(message):
    global main_command
    global data
    global idupdate
    print(data)
    if message.text == "add" or main_command == 'add':
        main_command = "add"
        if message.text == "add":
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
            add_car(data[message.chat.id])
            data[message.chat.id] = {
                "model": None,
                "prod_year": None,
                "color": None
            }
            bot.send_message(message.chat.id, f"Car object added succesifully!")
    elif message.text == "get-all":
        cars = get_cars()
        msg = ""
        for car in cars:
            msg += f"id: {car[0]}\nmodel: {car[1]}\nprod year: {car[2]}\ncolor: {car[3]}\n"
        bot.send_message(message.chat.id, msg)
    elif message.text == "update" or main_command == "update":
        main_command = "update"
        if message.text == "update":
            bot.send_message(message.chat.id, "Cars id: ")
        elif idupdate == None:
            idupdate = message.text
            bot.send_message(message.chat.id, "New model cars: ")
        elif data[message.chat.id]['model'] == None:
            data[message.chat.id]['model'] = message.text
            bot.send_message(message.chat.id, "New prod year cars: ")
        elif data[message.chat.id]['prod_year'] == None:
            data[message.chat.id]['prod_year'] = message.text
            bot.send_message(message.chat.id, "New color cars: ")
        elif data[message.chat.id]['color'] == None:
            data[message.chat.id]['color'] = message.text
            print(data)
            update(data[message.chat.id],idupdate)
            main_command = None
            data[message.chat.id] = {
                "model": None,
                "prod_year": None,
                "color": None
            }
            idupdate = None
    else:
        bot.send_message(message.chat.id, "Else")








bot.infinity_polling()