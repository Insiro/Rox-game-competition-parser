import requests
from bs4 import BeautifulSoup
import json
import Month_to_NUM as con

link = 'https://lol.gamepedia.com/Leaguepedia:Tournaments'
req = requests.get(link)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
lists = list()
tags = '#mw-content-text > div > div > div > div > table > tbody > tr:nth-child(2) > td > div > div'

i = 0
datr = dict()
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
            lists.append({'start': Sdata, 'end': Edata, 'name': label.text})
        i = 0 if i == 2 else i+1


output = open('lol.gamepedia.json', 'w')
output.write(json.dumps(lists))
output.close
