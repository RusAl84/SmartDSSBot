from os import fchdir
from webbrowser import get
import telebot;

bot = telebot.TeleBot('5111904045:AAH8VIo6dXf1Uz-CddZ818PUOWXzoF0j6t8');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    helpStr="Привет, это проект SmartDSSBot - Интеллектуальный Telegram Бот для помощи в выборе смартфона. \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if fc:
        
    elif str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        str1="SmartDSSBot - Интеллектуальный Telegram Бот для помощи в выборе смартфона. \n Список команд: "\
            "\n /s - начать подбор \n Для информации введите /help."
        bot.send_message(message.from_user.id, str1) 
    elif str(message.text).lower() == "\s":
        fc=True
        fm=False
        fd=False
        bot.send_message(message.from_user.id, "Введите минимальную имаксимальную стоимость (в рублях):")
    else:
        bot.send_message(message.from_user.id, helpStr)

bot.polling(none_stop=True, interval=0)