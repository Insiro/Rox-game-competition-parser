import requests
from bs4 import BeautifulSoup
import json
import Month_to_NUM as con
import checkStatus as CS
from datetime import datetime
import lol_gamepedia_Extention as LE


def parse():
    year = str(datetime.today().year)
    hostname = 'https://lol.gamepedia.com'
    link = 'https://lol.gamepedia.com/Leaguepedia:Tournaments'
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = list()
    tags = '#mw-content-text > div > div > div > div > table > tbody > tr:nth-child(2) > td > div > div'

    if CS.check(link) != 0:
        output = open('lol.gamepedia.json', 'w')
        output.write(json.dumps([None]))
        output.close
        return -1
    i = 0
    for div in soup.select(tags):
        for labels in div.select('div > table > tbody > tr'):
            th = labels.select('th')
            if th != None and th == 'PAST':
                continue
            for label in labels.select('td'):
                if i == 0:
                    date = label.text.split(" ")
                    Sdata = year+con.Short(date[0])+"%02d" % int(date[1])
                    if(date[2] != '-' or date[3] == '??'):
                        Edata = None
                    else:
                        Edata = year+con.Short(date[3]) + "%02d" % int(date[4])
                elif i == 1:
                    temLink = hostname + label.a['href']
                    lists.append(
                        {'start': Sdata, 'end': Edata, 'name': label.a.text, 'link': temLink, 'data': LE.parse(temLink)})
                i = 0 if i == 2 else i+1

    output = open('lol_gamepedia.json', 'w')
    output.write(json.dumps(lists))
    output.close
    return 0


parse()
