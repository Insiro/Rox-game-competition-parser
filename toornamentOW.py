import requests
from bs4 import BeautifulSoup
import jsonout as JO
import checkStatus as CS


def parse():
    link = 'https://www.toornament.com/games/overwatch'
    tag = '#tournament-game-list-tab > section > div'
    if CS.check(link) != 0:
        JO.output('toornament.json', [None])
        return -1
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    lists = list()
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
    JO.output('toornament.json', lists)
    return 0
