from os import fchdir
from webbrowser import get
import telebot;
import json
import copy


bot = telebot.TeleBot('5111904045:AAH8VIo6dXf1Uz-CddZ818PUOWXzoF0j6t8');



global aList
aList=[]
global qList
qList=[]
global fc
global fm
global fd
fc=False
fm=False
fd=False


def fCost(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if int(item ['cost']) >=minp and int(item ['cost']) <=maxp:
            fList.append(item)
    qList=copy.deepcopy(fList)
    
def fRam(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if int(item ['mram']) >=minp*1024 and int(item ['mram']) <= maxp*1024:
            fList.append(item)
    qList=copy.deepcopy(fList)

def fDiag(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if float(item ['screen diagonal']) >=float(minp) and float(item['screen diagonal']) <= float(maxp):
            fList.append(item)
    qList=copy.deepcopy(fList)

def printJson():
    global qList
    str1=""
    for item in qList:
        # cloth=item['cloth']
        str1+="\n"+"Фирма: " + item['brand'] +" \n Модель: " +item['model']+" \n Цена: "+ item['cost'] + ""\
        "\n Объем RAM: " + item['ram'] + " Диагональ экрана: "  + item['screen diagonal'] + ""\
        "\n Описание: "+ item['description'] + "\n"
    return str1


def initData():
    global aList
    global qList
    fileObject = open ("data.json",  "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    qList=copy.deepcopy(aList)
    


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global fc
    global fm
    global fd
    helpStr="Привет, это проект SmartDSSBot - Интеллектуальный Telegram Бот для помощи в выборе смартфона. \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if fc:
        initData()
        fCost(splitted_text[0], splitted_text[1])
        fc=False
        fm=True
        fd=False
        bot.send_message(message.from_user.id, "Введите минимальное и максимальное количество RAM (в Гб):")
    if fm:
        fRam(splitted_text[0], splitted_text[1])
        fc=False
        fm=False
        fd=True
        bot.send_message(message.from_user.id, "Введите минимальную и максимальную диагональ (в дюймах):")
    if fd:
        fDiag(splitted_text[0], splitted_text[1])
        fc=False
        fm=False
        fd=False
        str1  = "/n ПО Вашему запросу Вам подойдут: \n\n" + printJson()
        bot.send_message(message.from_user.id, str1)
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
        bot.send_message(message.from_user.id, "Введите минимальную и максимальную стоимость (в рублях):")
    else:
        bot.send_message(message.from_user.id, helpStr)


bot.polling(none_stop=True, interval=0)