import requests
from bs4 import BeautifulSoup
import checkStatus as CS
import datetime
testl = 'https://lol.gamepedia.com/index.php?title=Special:RunQuery/MatchCalendarExport&MCE%5B1%5D=Rift+Rivals+2019%2FNA-EU&pfRunQueryFormName=MatchCalendarExport'
tag = '#mw-content-text > div.mw-parser-output > pre > span[class=TimeInLocal]'


def parse(link):
    status = CS.check(link)
    if status != 0:
        return None
    lists = list()
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    for block in soup.select(tag):
        tetime = block.text.split(',')
        time = datetime.datetime(int(tetime[0]), int(tetime[1]), int(
            tetime[2]), int(tetime[3]), int(tetime[4]))
        time += datetime.timedelta(hours=+9)

        lists.append([time.strftime('%Y%m%d'), time.strftime('%H:%M')])
    return lists


print(parse(testl))
