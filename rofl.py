from random import randrange as rnd

rofles=(
    """Проснулись эльфы, и увидели звезды, ибо лежали на спине, и полюбили звезды и ночь.\n
Проснулись люди, и увидели восходящее солнце, ибо лежали на боку, и полюбили солнце и день.\n
Проснулись гномы, и не увидели ничего, ибо лежали носом в землю, и подумали: зачем же надо было вчера так напиваться?""",
    "Дварфийский анекдот: Вы называете свою цену. Я называю свою цену. Потом мы оба смеемся и приступаем к серьезному разговору.",
)

def getRofl():
    return str(rofles[rnd(len(rofles))])