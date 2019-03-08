import  os
import http.client, urllib.parse
from random import randrange as rnd
#The code is based on the official example from the Microsoft Azure-Samples repository. For personal use only

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey =os.getenv("BINGKEY")

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing search instance in your Azure dashboard.



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

def getSearch(qu="NOQUERY"):
    if qu=="NOQUERY":
        qu=rofles[0][rnd(len(rofles[0]))]+" "+rofles[1][rnd(len(rofles[0]))]
    print("ЗАПРОС: "+qu)
    return getLink(qu)

def getLink(qu="cat"):
    host = "api.cognitive.microsoft.com"
    path = "/bing/v7.0/images/search"

    term = qu
    if len(subscriptionKey) == 32:
        links = []
        print('Searching images for: ', term)

        headers, result = BingImageSearch(term,host,path)
        # print("\nRelevant HTTP Headers:\n")
        # print("\n".join(headers))
        # print("\nJSON Response:\n")
        # print(json.dumps(json.loads(result), indent=4))
        print(type(result))
        for r in result.split("contentUrl"):
            r = r.replace(": \"", "")
            ri = r.find("\", ")
            link = r[1:ri]
            link = link.replace("\/", "/")
            if link.rfind("?") != -1:
                link = link[:link.rfind("?")]
            links.append(link)
        # print(links)
        links.pop(0)
        # print (links)
        try:
            return links[rnd(len(links)//2)]
        except ValueError:
            return getRofl()
    else:

        print("Invalid Bing Search API subscription key!")
        print("Please paste yours into the source code.")
        return "Oops! Not find!"

def BingImageSearch(search,host= "api.cognitive.microsoft.com",path= "/bing/v7.0/images/search"):
    "Performs a Bing image search and returns the results."

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")


if __name__ == '__main__':
    print(getRofl())
    #while True:

#        for img in res["items"]:
#            print(img["link"])
#
#        if "nextPage" not in res["queries"]:
#            break

 #       start = res["queries"]["nextPage"][0]["startIndex"]