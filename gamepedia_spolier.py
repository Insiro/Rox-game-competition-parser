import requests
from bs4 import BeautifulSoup
import datetime
import checkStatus as CS

testlink = 'https://pubg-esports.gamepedia.com/Special:RunQuery/SpoilerFreeSchedule?SFS%5B1%5D=National%20PUBG%20League/2019%20Season/NPL%20Royale%201&pfRunQueryFormName=SpoilerFreeSchedule'
tag = '#mw-content-text > div.mw-parser-output > table > tr'


def parse(link):
    if CS.check(link) != 0:
        return None
    lists = list()
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    j = 1
    for block in soup.select(tag):
        i += 1
        if block.has_attr('class'):
            if block.th != 'Round':
                j = 0
                for atrr in block.select('td'):
                    j += 1
                    if j == 4:
                        temp = atrr.span.text.split(',')
                        date = datetime.datetime(
                            int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]))
                        time = date.strftime('%Y%m%d')
                    elif j == 7:
                        lists.append([time, atrr.text[:-1]])
    return lists
