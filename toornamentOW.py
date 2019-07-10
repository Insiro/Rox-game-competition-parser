import requests
from bs4 import BeautifulSoup
import jsonout as JO
import checkStatus as CS
import datetime


def parse():
    hostname = 'https://www.toornament.com'
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
        for label in div[i].select('div > a'):
            link = hostname+label['href']
            table = label.select('div')
            name = table[1].div.text
            i = 0
            start = end = None
            for date in table[6].select('div > date-view'):
                temp = date['value'].split('-')
                if i == 1:
                    start = datetime.datetime(int(temp[0]), int(
                        temp[1]), int(temp[2])).strftime('%Y%m%d')
                    i += 1
                elif i == 2:
                    end = datetime.datetime(int(temp[0]), int(
                        temp[1]), int(temp[2])).strftime('%Y%m%d')
            i = 0
            team = table[5].span.text[:-1]
            lists.append({'start': start, 'end': end,
                          'name': name, 'link': link, 'date': {'Organizer': None, 'Number of Teams': team, 'Links': None,
                                                               'Region': regin, 'Type': types, 'Streams': None, 'Schedule': None}})
    JO.output('toornamentOW.json', lists)
    return 0


parse()
