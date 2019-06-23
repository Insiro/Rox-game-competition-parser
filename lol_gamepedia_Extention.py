import requests
from bs4 import BeautifulSoup
import checkStatus as CS

def parse(link):
    status = CS.check(link)
    if status != 0:
        return None
    texts = 'Nan'
    temp = 'Nan'
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    heads = {'Organizer', 'Prize Pool', 'Region', 'Event Type',
             'Links', 'Streams', 'Schedule'  # , 'Sponsor(s)'
             }
    tag = '#infoboxTournament > tbody > tr > td'
    data = {'Organizer': None, 'Number of Teams': None, 'Prize': None, 'Region': None,
            'Type': None, 'Links': None, 'Streams': None, 'Schedule': None  # ,'Sponsors': None
            }
    for block in soup.select(tag):
        texts = block.text
        if len({texts} & heads) != 0:
            temp = texts
        elif temp != 'Nan':
            if temp == 'Links':
                data[temp] = {'name': block.text, 'link': block.a['href']}
            elif temp == 'Organizer':
                data[temp] = list()
                for a in block.select('td > a'):
                    data[temp].append(
                        {'name': a.text, 'link': None if a['href'][0] == '/' else a['href']})
            elif temp == 'Streams' or temp == 'Sponsor(s)':
                if temp == 'Sponsor(s)':
                    temp = 'Sponsors'
                data[temp] = list()
                if block.a != None:
                    for a in block.select('a'):
                        data[temp].append({'name': a.text, 'link': a['href']})
            elif temp == 'Schedule':
                data[temp] = block.a['href']
            else:
                if temp == 'Event Type':
                    temp = 'Type'
                data[temp] = block.text.split(
                    '\xa0')[1] if temp == 'Region' else block.text
            temp = 'Nan'

    return data