import requests
from bs4 import BeautifulSoup
import json
import Month_to_NUM as con
import checkStatus as CS


def parse():
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
        for label in div.select('td'):
            if i == 0:
                date = label.text.split(" ")
                Sdata = con.Short(date[0])+"."+date[1]
                if(date[2] != '-' or date[3] == '??'):
                    Edata = None
                else:
                    Edata = con.Short(date[3]) + "."+date[4]
            elif i == 1:
                lists.append(
                    {'start': Sdata, 'end': Edata, 'name': label.text})
            i = 0 if i == 2 else i+1

    output = open('lol_gamepedia.json', 'w')
    output.write(json.dumps(lists))
    output.close
    return 0
