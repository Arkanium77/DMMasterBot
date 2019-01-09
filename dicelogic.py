from random import randrange as rnd
import re

diceTypes = [[2, "C","С"], 3, "F", 4,6, 8, 10, 12, [20, "D"], 100]

NO = 'NO'


def diceMaster(s):
    s = s.split('d')
    for i in range(len(s)):
        s[i] = s[i].upper()
    if (len(s) == 1):
        s.append(s[0])
        s[0] = 1
    print(s)
    if (len(s) != 2):
        return NO
    dices = diceRule(s[1])
    print("dices -> ", dices)
    type = typeRule(dices[0])
    print("type -> ", type)
    if type == NO:
        return NO
    if (type == "F"):
        throws = throw(type, 4)
        t = 0
        for i in throws:
            t += i
        if (len(dices) > 1):
            for j in dices[1:]:
                t += int(j)
        return [t]
    quant = quantRule(s[0])
    print("quant -> ", quant)
    throws = throw(type, quant)
    print("throws -> ", throws)

    if len(dices) > 1 and (type != 2 or type != "2"):
        for i in range(len(throws)):
            for j in dices[1:]:
                throws[i] += int(j)

    elif type == 2 or type == "2":
        for i in range(len(throws)):
            if throws[i] == 0:
                throws[i] = "tails"
            else:
                throws[i] = "heads"
    print("throws+ -> ", throws)
    return throws


def diceRule(s):
    dices = s.replace("-", "+-")
    dices = dices.split("+")
    return dices


def typeRule(s):
    print("TypeRule: " + s)
    if (s == "F"):
        return s
    try:
        s = int(s)
    except:
        pass
    type = NO
    for i in diceTypes:
        print(i, "  ->  ", s)
        if i == s:
            type = i
            print("+")
            return type
        else:
            try:
                print(inList(i, s))
            except Exception:
                continue
            if inList(i, s):
                type = i[0]
                print("+")
                return type

        print("next")
    return type


def inList(list, el):
    for i in list:
        if i == el:
            return True
    return False


def quantRule(s):
    if (len(s) == 0):
        return 1
    if (int(s) > 0):
        return int(s)
    return NO


def throw(type, quant):
    if type == "F":
        a = []
        for i in range(0, 4):
            a.append(rnd(-1, 2))
        return a
    if type == "2" or type==2:
        a = []
        for i in range(0, int(quant)):
            a.append(rnd(0, type))
        return a
    a = []
    for i in range(0, int(quant)):
        a.append(rnd(1, type + 1))
    return a