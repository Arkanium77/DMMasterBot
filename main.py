import requests
import telebot
import os
from dicelogic import diceMaster
from excuse import genEx
from triumf import getGrats
from triumf import clean
from late import howLate
from searcher2 import getRofl
import re
from others.consts_tg import d20
from others.consts_tg import coin
from others.consts_tg import manul
from random import randrange as rnd
from flask import Flask, request

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

diceR = "[0-9]*d(2|C|c|3|F|4|6|8|10|12|20|D|d|100)[0-9^(+\-)]*"
server = Flask(__name__)


@bot.message_handler(regexp=diceR)
def handle_message(message):
    if isReply(message):
        return
    s = message.text
    tst = re.sub(diceR, "!", s)
    if (tst == "!"):
        if s=="1d20" or s=="d20" :
            stickerDice(message)

        else:
            a = diceMaster(s)
            print(message)
            bot.reply_to(message, messBuilder(message, a))
    pass


@bot.message_handler(regexp="/rofl.*")
def handle_q(message):
    if isReply(message):
        return
    print("ROFLTIME")
    s=message.text
    if s[:5]=="/rofl":
        if(len(s)>=7):
            link=getRofl(s[6:])
            print(s[6:])
            bot.send_message("-1001404839900",s[6:])
        else:
            link=getRofl()
        response = requests.get(link)
        photo = response.content
        bot.send_photo(message.chat.id, photo)


'''
lateR=re.compile(".*(опазд|опозд|задержу|задержим).*",re.MULTILINE | re.IGNORECASE)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
'''


def lMatch(message):
    lateR = re.compile(".*(опазд|опозд|задержу|задержим).*", re.MULTILINE | re.IGNORECASE)
    try:
        if re.search(lateR, message.text) == None:
            return False
    except Exception:
        return False

    return True

def isReply(message):
    if message.forward_from!=None or message.forward_from_chat!=None:
        return True
    return False

@bot.message_handler(func=lMatch)
def latecatch(message):
    late(message)


def messBuilder(message, a):
    s = ""

    str1 = message.from_user.username

    try:
        str1 += "  throws:\n"
    except Exception:
        str1 = message.from_user.first_name
        str1 += "  throws:\n"
    s += str1
    for i in a:
        s += str(i) + "     "
    # s+="\n"
    return s


@bot.message_handler(commands=['excuse'])
def excuse(message):
    if isReply(message):
        return
    s = genEx()
    bot.reply_to(message, s)

@bot.message_handler(commands=['throw'])
def stickerDice(message):
    if isReply(message):
        return
    s=diceMaster("1d20")
    bot.send_sticker(message.chat.id, d20[s[0]-1])

@bot.message_handler(commands=['flip'])
def stickerCoin(message):
    if isReply(message):
        return
    s=diceMaster("1d2")
    if s[0]=="heads":
        bot.send_sticker(message.chat.id, coin[0])
    else:
        bot.send_sticker(message.chat.id, coin[1])


@bot.message_handler(commands=['late'])
def late(message):
    if isReply(message):
        return
    s = howLate()
    bot.reply_to(message, s)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if isReply(message):
        return
    print(message)
    str = ""
    if (message.from_user.language_code == "ru"):
        str += """
		Привет!\n
		Этот бот создан для всех любителей ролевых игр. Он умеет бросать кости. Запросы к боту следует отправлять в формате:\n
		1d4\n
		d20\n
		5d8+4-2\n
		\n
		Бот поддерживает следующие типы костей:\n
		d2 или dC - монетка (Heads\Орёл = 1, Tails\Решка = 0)\n
		dF - FUDGE Dice. Происходит бросок сразу 4х дайсов\n
		d4, d8, d10, d12, d20, d100\n
		"""
    else:
        str += """
		Hello!\n
		This bot is created for all fans of role-playing games. He can throw dices. Requests to the bot should be sent in the following format:\n
		1d4\n
		d20\n
		5d8 + 4-2\n
		\n
		The bot supports the following dice types:\n
		d2 or dC - coin (Heads = 1, Tails = 0)\n
		dF - FUDGE Dice. 4 dice throws right away\n
		d4, d8, d10, d12, d20, d100\n
		"""
    bot.reply_to(message, str)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    if re.search(r"((ужасы войны)|(ужасывойны))", message.text, re.MULTILINE | re.IGNORECASE):
        bot.reply_to(message, "Ужасы войны, ужасы войны, ужасы войны...")
    elif re.search(r"монет|coin|золот|серебрян|медн", message.text, re.MULTILINE | re.IGNORECASE):
        bot.reply_to(message, "Монетка-монетка!")
    elif re.search(r"поздрав|грац|молодцы|молодец|молодцо", message.text, re.MULTILINE | re.IGNORECASE):
        grace(message)
    elif re.search(r"манул|manul", message.text, re.MULTILINE | re.IGNORECASE):
        manul(message)
    pass

def manul(message):
    id = message.chat.id
    for i in range(rnd(6)):
        bot.send_sticker(id,manul)

def grace(message):
    if "re" in message.text:
        clean()
        return

    id=message.chat.id
    t=message.date
    ms=getGrats(id,t)
    bot.send_message(id, ms)


# apihelper.proxy = {'https': 'https://67.205.146.54:80'}
# apihelper.proxy = {'https': 'socks5://swcbbabh:aYEbh6q5gQ@bb8.vivalaresistance.info:3306'}
@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://dmmasterbot.herokuapp.com/' + token)
    return "!", 200


if __name__ == '__main__':

    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    '''
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("BOOM")
            time.sleep(3)
    '''


#pip freeze > requirements.txt
