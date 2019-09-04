import requests
from bs4 import BeautifulSoup
import Month_to_NUM as con
import checkStatus as CS
import gamepedia_spolier as GS

testlink = 'https://wcs.starcraft2.com/tournament/5131/'


def parse(link):
    status = CS.check(link)
    data = {'Organizer': None, 'Number of Teams': None, 'Links': None,
            'Region': None, 'Type': None, 'Tier': None, 'Prize Pool': None, 'Streams': None, 'Schedule': None}
    if status != 0:
        return None
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pTag = soup.find_all('p', class_='quarantine-block')
    for i in pTag:
        if 'Overall' in i.text:
            data['Prize Pool'] = i.text[8:]
    return data
