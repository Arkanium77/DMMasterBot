from random import randrange as rnd

maxtime = 40000

timeLen = [
    ["мин", 60],
    ["час", 3600],
    ["ден", 86400],
    ["недел", 604800],
]

start = [
    "Будет через",
    "Опоздает на",
    "Задержится на",
    "Будет очень скоро! Всего через",
    "Уже на подходе. Осталось всего",
    "Мчится на всех парах! Будет через",
]


def maxTimeIndex(time):
    for i in range(len(timeLen)):
        if (time % timeLen[i][1] == time):
            print(i - 1)
            return i - 1
    return len(timeLen) - 1


def times(it, time):
    mas = []
    while it > -1:
        print(time, "//", timeLen[it][1], "=", time // timeLen[it][1])
        c = time // timeLen[it][1]
        mas.append(c)
        time = time % timeLen[it][1]
        it -= 1
    mas.append(time)
    return mas


def trueTime(time):
    iit = maxTimeIndex(time)
    m = times(iit, time)
    print(m)
    sec=m.pop()
    print(sec)
    m.reverse()
    m.append(sec)
    print("Reverse mas=",m)
    print(m)
    return m


def sEnd(c):
    if c>20:
        c%=10
    else:
        c%=20

    s = ""
    if c == 1:
        s += "у"
    elif c > 1 and c < 5:
        s += "ы"
    else:
        s += ""
    return "секунд" + s


def mEnd(c):
    if c > 20:
        c %= 10
    else:
        c %= 20
    s = ""
    if c == 1:
        s += "уту"
    elif c > 1 and c < 5:
        s += "уты"
    else:
        s += "ут"
    return "мин" + s


def hEnd(c):
    if c > 20:
        c %= 10
    else:
        c %= 20
    s = ""
    if c == 1:
        s += ""
    elif c > 1 and c < 5:
        s += "а"
    else:
        s += "ов"
    return "час" + s


def dEnd(c):
    if c > 20:
        c %= 10
    else:
        c %= 20
    s = ""
    if c == 1:
        s += "день"
    elif c > 1 and c < 5:
        s += "дня"
    else:
        s += "дней"
    return s


def wEnd(c):
    while c > 20:
        c -= 20
    s = ""
    if c == 1:
        s += "ю"
    elif c > 1 and c < 5:
        s += "и"
    else:
        s += "ь"
    return "недел" + s


def trueEnd(c, ty):
    s = ""
    if ty == timeLen[0][0]:
        s = mEnd(c);
    elif ty == timeLen[1][0]:
        s = hEnd(c);
    elif ty == timeLen[2][0]:
        s = dEnd(c);
    elif ty == timeLen[3][0]:
        s = wEnd(c);
    else:
        s = sEnd(c);
    return s


def namedTime(a):
    s = ""
    print("Это ", a)
    it = len(a) - 2
    while it >= 0:
        if (a[it] != 0):
            s += str(a[it]) + " " + trueEnd(a[it], timeLen[it][0]) + " "
        it -= 1
    if a[-1] != 0:
        s += str(a[-1]) + " " + trueEnd(a[-1], "секунд") + " "
    return s


def howLate(time="T"):
    if time == "T":
        time = rnd(62, maxtime)
    a = trueTime(time)
    name = namedTime(a)
    return start[rnd(len(start))] + " " + name


if __name__ == '__main__':
    s = "Я опоздаю немного"
    print(howLate(int(input(">"))))
    while True:
        print(howLate(int(input(">"))))
