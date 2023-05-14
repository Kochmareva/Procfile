import telebot
from telebot import types
import config

Token = "6046267841:AAHfuw9k8kjpIP6YMWB8S01lfaKGvSwtbCQ"
bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать расписание")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Рады Вас видеть, {0.first_name}! Вы хотите узнать расписание?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Узнать расписание"):
        bot.send_message(message.chat.id, text="В какой город Вы направляетесь? Выберите ниже👇")
        btn1 = types.KeyboardButton("д. Андреевка")
        btn2 = types.KeyboardButton("с. Новоипатово")
        btn3 = types.KeyboardButton("п. Бобровский")
        btn4 = types.KeyboardButton("п. Двуреченск")
        btn5 = types.KeyboardButton("ст. Седельниково")
        btn6 = types.KeyboardButton("п. Первомайский")
        btn7 = types.KeyboardButton("г. Екатеринбург")
        btn8 = types.KeyboardButton("г. Арамиль")
        btn9 = types.KeyboardButton("Внутри города")

    elif (message.text == "д. Андреевка"):
        bot.send_message(message.chat.id, "Расписание маршрута №103 Сысерть - Андреевка", "5:00", "7:50", "14:10", "19:00", sep="\n")

    elif (message.text == "с. Новоипатово"):
        bot.send_message(message.chat.id, "Расписание маршрута №103-А Сысерть - Новоипатово", "5:10", "7:30", "12:50", "17:15", sep="\n")

    elif (message.text == "п. Бобровский"):
        bot.send_message(message.chat.id, "Расписание маршрута №106 Сысерть - Бобровский", "6:40", "9:30", "13:40", "18:40", sep="\n")

    elif (message.text == "п. Двуреченск"):
        bot.send_message(message.chat.id, "Расписание маршрута №109 Сысерть - Двуреченск", "5:10", "7:40", "13:10", "18:10", sep="\n")

    elif (message.text == "ст. Седельниково"):
        bot.send_message(message.chat.id, "Расписание маршрута №155 Сысерть - ст. Седельниково", "5:00", "9:20", "13:50", "18:30", sep="\n")

    elif (message.text == "п. Первомайский"):
        bot.send_message(message.chat.id, "Расписание маршрута №155-А Сысерть - Первомайский", "5:25", "8:05", "13:45", "18:50", sep="\n")

    elif (message.text == "г. Екатеринбург"):
        bot.send_message(message.chat.id, "Расписание маршрутов Сысерть - г. Екатеринбург", "№160-Б 5:41",
                         "№134(через г.Арамиль) 6:21", "№160-Б 6:30", "№130-Б 6:51", "№161(через п.Октябрьский) 7:25",
                         "№160-Б 8:15", "№161(через п.Октябрьский) 9:40", "№130-Б 11:05", "№161(через п.Октябрьский) 11:30",
                         "№160-Б 12:07", "№134(через г.Арамиль) 12:15", "№160-Б 12:50", "№161(через п.Октябрьский) 13:09",
                         "№161(через п.Октябрьский) 14:35", "№160-Б 15:17", "№134(через г.Арамиль) 15:50", "№160-Б 16:00",
                         "№130-Б 16:23", "№161(через п.Октябрьский) 17:25", "№160-А 17:58", "№161(через п.Октябрьский) 18:30",
                         "№161(через п.Октябрьский) 20:38", sep="\n")

    elif (message.text == "г. Арамиль"):
        bot.send_message(message.chat.id, "Расписание маршрута №132 Сысерть - г. Арамиль", "8:30", "11:45", "14:50", "17:05", "19:00", sep="\n")

    elif (message.text == "Внутри города"):
        btn1 = types.KeyboardButton("Маршрут №1С")
        btn2 = types.KeyboardButton("Маршрут №1К")
        btn3 = types.KeyboardButton("Маршрут №2")
        btn4 = types.KeyboardButton("Маршрут №3")
        bot.send_message(message.chat.id, "Выберите нужный маршрут👇")

    elif (message.text == "Маршрут №1С"):
        bot.send_message(message.chat.id, "Расписание маршрута №1 ул.Самстроя", "6:35", "7:40", "8:40", "9:40", "10:40",
                         "12:40", "13:40", "14:40", "16:40", "17:40", "18:40", "19:40", sep="\n")

    elif (message.text == "Маршрут №1К"):
        bot.send_message(message.chat.id, "Расписание маршрута №1 ул.Коммуны", "6:40", "7:40", "8:40", "9:40", "10:40",
                         "12:40", "13:40", "14:40", "16:40", "17:40", "18:40", "19:40", sep="\n")

    elif (message.text == "Маршрут №2"):
        bot.send_message(message.chat.id, "Расписание маршрута №2", "6:40", "7:20", "8:00", "8:40", "9:20",
                         "10:00", "12:10", "12:50", "13:30", "14:10", "14:50", "16:35", "17:15", "17:55", "18:40", sep="\n")

    elif (message.text == "Маршрут №3"):
        bot.send_message(message.chat.id, "Расписание маршрута №3", "7:40", "8:30", "9:20", "11:10", "12:00", "12:50",
                         "13:40", "14:30", "16:00", "16:50", "17:40", "18:30", sep="\n")

    else:
        bot.send_message(message.chat.id, text="Некорректный ввод...")


bot.polling(none_stop=True)