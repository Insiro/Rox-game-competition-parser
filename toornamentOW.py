import requests
from bs4 import BeautifulSoup
import json
import checkStatus as CS


def parse():
    link = 'https://www.toornament.com/games/overwatch'
    if CS.check(link) != 0:
        with open('toornament.json', 'w') as output:
            output.write(json.dumps([None]))
        return -1
    tag = '#tournament-game-list-tab > section > div'
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    lists = list()
    OWoutput = open('toornament.json', 'w')

    div = soup.select(tag)
    for i in range(2, 5):
        j = 0
        for label in div[i].select('div > a > div'):
            j += 1
            if j == 2:
                name = label.select('div')[0].text
            elif j == 3:
                k = 1
                end = None
                for timetag in label.select('div > time'):
                    if k == 1:
                        start = ''.join(timetag['datetime'].split('-'))
                    else:
                        end = ''.join(timetag['datetime'].split('-'))
                    k = -k
            elif j == 5:
                lists.append({'start': start, 'end': end, 'name': name})
                j = 0
    OWoutput.write(json.dumps(lists))
    OWoutput.close()
    return 0
