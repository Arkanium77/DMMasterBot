from random import randrange as rnd
excuses=[
    [   #Начало
        "Не, я пас.",
        "Я сегодня не смогу,",
        "Хз. Не думаю, что получится...",
        "Я конечно попробую, но, скорее всего, нет.",
        "Не смогу.",
        "Не получится.",
        "Попытаюсь, но",
        "Может быть, но",
        "Не в этот раз.",
        "Кто знает. Но... ",
    ],
    [   #причины
        "учёба",
        "у меня учёба",
        "у бабушки день рождения",
        "у дяди день рождения",
        "у дедушки день рождения",
        "у кота день рождения",
        "у моего первого ДМа день рождения",
        "у Ктулху день рождения",
        "на работе завал",
        "работы много",
        "придётся много работать",
        "слишком рано вставать",
        "очень лень",
        "болею",
        "я болею",
        "еду к стоматологу",
        "у меня лекция как раз в это время",
        "нужно подготовить мой бункер к зомби-апокалипсису",
        "дел так много... Может я опоздаю часов на 20",
        "как раз в это время я планирую ничего не делать",
        "у меня планы",
        "столько работы навалилось",
        "я не в городе",
        "я не в России",
        "полиция окружила мой дом, не знаю, когда они поймут, что тот человек сам упал на нож 20 раз",
        "у меня проявилась аллергия на окружающий мир",
        "голоса в моей голове... Они этого не хотят... Эх",
    ],
    [   #дополнение
        ", к тому же",
        ", да ещё и",
        ", кроме того",
        ", а ещё",
        ", да и к тому же",
        ",",
        ",",
        ", и ",
        ", да и",
        ", а кроме того",
        ", ещё",
        ", такие дела... А ещё",
        ", такие дела... Да и",
    ],
    [   #завершение
        ", так что никак.",
        ", жаль, но не выйдет.",
        ", совсем не выходит.",
        ". Как-то не выходит",
        ". Не получится",
        ". Вообще никак.",
        ". Может, в другой раз..."
        ". Такие дела.",
        ". Не выходит.",
        ". Простите.",
        ", так что сорян.",
        ". В этот раз без меня.",
        ". В следующий раз обязательно.",
        ". Так что я на связи, вы отпишитесь потом.",
        ". Напишите как отыграете обязательно, интересно же.",
    ]
]


def cDrop():
    if rnd(2)==1: return True
    return False

def genEx(a=excuses,d=0,s=""):
    if d==0:
        d = rnd(1, len(excuses))
    print("d =",d)
    s=""
    for i in range(d+1):
        if i==2:
            s = genIt(a, 2, s)
            s = genIt(a, 1, s)
            while cDrop():
                s = genIt(a, 2, s)
                s = genIt(a, 1, s)
                t = rnd(1)
        else:
            s=genIt(a,i,s)
    if s[-1]!="." or s[-2]!=".":
        s+="."
    return s


def genIt(a,d,s):
    #print ("genIt(",d,")")
    s1=a[d][rnd(len(a[d]))]
    if  s=="":
        #print("S - пустая")
        s1 = s1[0].upper() + s1[1:]
    else:
        if s[-1]=="." or s[-2]==".":
            #print("последний в s  - точка")
            #print(s1)
            s1=s1[0].upper()+s1[1:]
            #print(s1)
        if s1[0]!=",":
            #print("первый символ не запятая")
            s1=" "+s1
    #print("s="+s)
    #print("s1="+s1)
    return s+s1


if __name__ == '__main__':
    s=""
    d=rnd(1,len(excuses))
    s=genEx(excuses,d,s)
    print(s)