import telebot
import os
from telebot import apihelper
from dicelogic import diceMaster
import time
import re
from flask import Flask, request

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

diceR = "[0-9]*d(2|C|c|3|F|4|6|8|10|12|20|D|d|100)[0-9^(+\-)]*"

server = Flask(__name__)


@bot.message_handler(regexp=diceR)
def handle_message(message):

    s = message.text
    tst = re.sub(diceR, "!", s)
    if (tst == "!"):
        a = diceMaster(s)
        # print(message)
        bot.reply_to(message, messBuilder(message, a))
    pass

def messBuilder(message, a):
    s = ""
    str1 = message.from_user.username
    str1 += "  throws:\n"
    s += str1
    for i in a:
        s += str(i) + "     "
    # s+="\n"
    return s

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
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
    print(message.text)
    if re.search(r"((ужасы войны)|(ужасывойны))", message.text, re.MULTILINE | re.IGNORECASE):
        bot.reply_to(message, "Ужасы войны, ужасы войны, ужасы войны...")
    pass


#apihelper.proxy = {'https': 'https://67.205.146.54:80'}
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
