from random import randrange as rnd
import time
triumph=[
    "Я тоже присоединяюсь к поздравлениям!",
    "Грац",
    "Вау! Круто! Поздравляю!",
    "Это же просто ЛЕГЕНДАРНО! Поздравляю!",
    "#поздравление",
    "11010000 10011111 11010000 10111110 11010000"
    + " 10110111 11010000 10110100 11010001 10000000 11010000 10110000 11010000 "
    + "10110010 11010000 10111011 11010001 10001111 11010001 10001110. \nЧто значит на языке ботов \"Поздравляю\"!",
    "Мои поздравления!",
    "Congratulations!",
    "Это так здорово! Поздравляю!",
    "Для такого случая у меня даже торт подготовлен. Шучу. Торт - это ложь.",
    "Это нужно отметить дварфийским пивом!",
    "Надо бы отметить!",
    "Двухсотлетнего эльфийского вина! Срочно! У нас тут праздник!",
    "Верите или нет, но я тоже очень хочу поздравить! Поздравляю!",
    "Эпично! Поздравляю!",
    "Будь я полуросликом - я бы закатил пир по этому поводу! Но я просто бот. <3",
    "Поздравляю! По такому случаю, выдайте человеку Легендарку. Срочно!",
    "Поздравляю! Пусть твои уровни растут так же быстро, как падает рубль.",
    "Мои поздравления! И пусть дорога приведет тебя в теплые пески",
    "Может ли бот чувствовать? Конечно. Например, я чувствую страшное желание поздравить кого нибудь!",
    "Поздравляю! Пусть кубы всегда ложатся как надо!",
    "В мире много счастливых дней. А этот особенно счастливый! Поздравляю!",
    "О, Господи, я так счастлив! Поздравляю!",
    "Поздравляю! Я просто без чувств! Практически присмерти от счастья."
    +" А единственное, что может спасти бота при смерти - это глоток бензина.",
    "Божественно! БОЖЕСТВЕННО! Поздравляю!",
    "Поздравляю! Пусть ДМ всегда будет милостив, а партия сжигает деревни.",
]
d={}
def clean():
    d.clear()

def getGrats(id,t):
    t=times(t)
    if d.get(id)==None:
        d[id]=t
        return triumph[rnd(len(triumph))]
    else:
        if d[id]!=t:
            d[id]=t
            return triumph[rnd(len(triumph))]
    return None

def times(t):
    t = time.ctime(t)
    t = t.split()
    return (t[1] + " " + t[2])

if __name__ == '__main__':
    #1546702082
    t=81242194
    id="Член"
    ms=getGrats(id,t)
    if ms!=None:
        print(ms)
    else:
        print("Не время для поздравлений")

    ms=getGrats(id,t)
    if ms!=None:
        print(ms)
    else:
        print("Не время для поздравлений")
    print()
    print(d)
    print()
    t=1546702082
    ms=getGrats(id,t)
    if ms!=None:
        print(ms)
    else:
        print("Не время для поздравлений")
    print()
    print(d)
    print()