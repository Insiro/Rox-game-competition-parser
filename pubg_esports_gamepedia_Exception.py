import requests
from bs4 import BeautifulSoup
import Month_to_NUM as con
import checkStatus as CS

keyord = {'Organizer', 'Number of Teams', 'Links', 'Region',
          'Type', 'Tier', 'Stream(s)'}
have_ln = {'Links', 'Stream(s)', 'Organizer'}
tag = '#infoboxTournament > tbody > tr > td'


def parsetest():
    parse('https://pubg-esports.gamepedia.com/FACEIT_Global_Summit_2019')


def parse(link):
    status = CS.check(link)
    if status != 0:
        return None
    req = requests.get(link)
    html = req.text
    texts = None
    soup = BeautifulSoup(html, 'html.parser')
    temp = 'Nan'
    data = {'Organizer': None, 'Number of Teams': None, 'Links': None,
            'Region': None, 'Type': None, 'Tier': None, 'Stream(s)': None}
    for block in soup.select(tag):
        texts = block.text
        if temp != 'Nan':
            if temp == 'Links'or temp == 'Organizer':
                data[temp] = {'name': block.text, 'link': block.a['href']}
            elif temp == 'Stream(s)':
                data[temp] = [{'name': block.a.text, 'link': block.a['href']}]
                if block.p != None:
                    for a in block.p.select('a'):
                        data[temp].append({'name': a.text, 'link': a['href']})
            else:
                if temp == 'Region':
                    data[temp] = block.text.split('\xa0')[1]
                else:
                    data[temp] = block.text
            temp = 'Nan'
        elif len(keyord & {texts}) != 0:
            temp = texts
    print(data)
    return data


parsetest()
