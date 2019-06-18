import requests
from bs4 import BeautifulSoup
import json


def toMonth(strs):
    if(strs == 'Jan'):
        return '1'
    elif(strs == 'Feb'):
        return '2'
    elif(strs == 'Mar'):
        return '3'
    elif (strs == 'Apr'):
        return '4'
    elif (strs == 'May'):
        return '5'
    elif (strs == 'Jun'):
        return '6'
    elif (strs == 'Jul'):
        return '7'
    elif (strs == 'Aug'):
        return '8'
    elif (strs == 'Sep'):
        return '9'
    elif (strs == 'Oct'):
        return '10'
    elif (strs == 'Nov'):
        return '11'
    elif (strs == 'Dec'):
        return '12'
    else:
        return -1


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
            Sdata = toMonth(date[0])+"."+date[1]
            if(date[2] != '-' or date[3] == '??'):
                Edata = None
            else:
                Edata = toMonth(date[3]) + "."+date[4]
        elif i == 1:
            lists.append({'start': Sdata, 'end': Edata, 'name': label.text})
        i = 0 if i == 2 else i+1


output = open('lol.gamepedia.json', 'w')
output.write(json.dumps(lists))
output.close