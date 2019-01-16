from googleapiclient.discovery import build
import os
from random import randrange as rnd

rofles=[
    [
        "ролевики настольные",
        "ролевики",
        "TRPG",
        "НРИ",
        "D&D",
        "DnD",
        "Dungeons and Dragons",
        "ДнД",
        "Подземелья и драконы"
    ],
    [
        "memes",
        "meme",
        "jokes",
        "comic",
        "comix",
        "humor",
        "tag yourself",
        "юмор",
        "мем",
        "шутка",
        "комикс"
    ]
]

def getRofl(qu="NOQUERY"):
    if qu=="NOQUERY":
        qu=rofles[0][rnd(len(rofles[0]))]+" "+rofles[1][rnd(len(rofles[0]))]
    print("ЗАПРОС: "+qu)
    return getLink(qu)

def getLink(qu="cat"):
    service = build("customsearch", "v1",
                    developerKey=os.getenv("DEVKEY"))
    start = 1
    res = service.cse().list(
        q=qu,
        cx=os.getenv("CX_KEY"),
        fileType="png,jpg,bmp,webp",  # bmp, gif, png, jpg, svg, pdf, ...
        imgColorType="color",  # mono, gray, color
        imgSize="large",  # icon, small, medium, large, xlarge, xxlarge, huge
        # imgType="photo",  # clipart, face, lineart, news, photo
        safe="off",  # high, medium, off
        searchType="image",
        start=start
    ).execute()
    print(res)



    link = res["items"][rnd(len(res["items"]))]["link"]
    try:
        it = str.rindex(link, "?")
    except Exception:
        it=len(link)
    print(link + "\nFullsize:  " + link[:it])
    return link[:it]

if __name__ == '__main__':
    while True:
        getLink()
#        for img in res["items"]:
#            print(img["link"])
#
#        if "nextPage" not in res["queries"]:
#            break

 #       start = res["queries"]["nextPage"][0]["startIndex"]