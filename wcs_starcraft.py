import requests
from bs4 import BeautifulSoup
import jsonout as JO
import checkStatus as CS
import datetime
import wcs_starcraft_Extention as ex


def parse():
    hostname = 'https://wcs.starcraft2.com'
    link = 'https://wcs.starcraft2.com/ko-kr/schedule/'
    if CS.check(link) != 0:
        JO.output('wcs_starcraft.json', [None])
        return -1
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = list()
    card = 'tileContainer-carousel'
    for block in soup.find('div', class_=card):
        for block2 in block.select('div'):
            blockLen = len(block2.select('div'))
            if blockLen < 1:
                continue

            div = block2.select('div > div')
            start_timestamp = int(div[0]['data-event-start-time'])
            start = datetime.datetime.fromtimestamp(start_timestamp/1000)
            if blockLen == 2:
                end_timestamp = int(div[0]['data-event-end-time'])
                end = datetime.datetime.fromtimestamp(end_timestamp/1000)
            name = div[1].text
            data_id = block2['data-tournament-id']
            link = hostname+'/tournament/'+data_id
            lists.append({'name': name, 'start': start.strftime('%Y%m%d'),
                          'end': end.strftime('%Y%m%d'), 'link': link, 'data': ex.parse(link)})
    JO.output('wcs_starcraft.json', lists)
    return 0
