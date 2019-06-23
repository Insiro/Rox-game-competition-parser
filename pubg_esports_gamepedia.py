# pubg-esports.gamepedia.com
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import Month_to_NUM as con
import checkStatus as CS
import pubg_esports_gamepedia_Exception as Ex
import jsonout as JO


def parse():
    year = str(datetime.today().year)
    hostname = 'https://pubg-esports.gamepedia.com'
    link = 'https://pubg-esports.gamepedia.com/PUBG_Esports_Wiki:Tournaments/'+year
    if CS.check(link) != 0:
        JO.output('pubg_esports_gamepedia.json', [None])
        return -1

    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = list()
    tags = '#mw-content-text > div > div > table > tbody > tr > td > div:nth-child(2)'
    for date in soup.select(tags+' > div'):
        temp = date.text
        if temp == 'UPCOMING' or temp == 'CURRENT' or temp == 'PAST' or temp == year:
            continue
        days = temp.split(' - ')
        start = days[0].split(' ')
        end = days[1].split(' ')
        lists.append({'start': year+con.Short(start[0])+"%02d" % int(start[1]), 'end': year+con.Short(
            end[0])+"%02d" % int(end[1]), 'name': None, 'link': None, 'data': None})
    name_list = soup.select(tags+' > span')
    for i in range(0, len(lists)):
        lists[i]['name'] = name_list[i].text
        temp = name_list[i].a['href']
        lists[i]['link'] = hostname+temp
        lists[i]['data'] = Ex.parse(hostname+temp)
    JO.output('pubg_esports_gamepedia.json', lists)
    return 0