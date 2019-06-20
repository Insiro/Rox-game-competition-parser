# pubg-esports.gamepedia.com
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import Month_to_NUM as con
import checkStatus as CS
import json


def parse():
    year = str(datetime.today().year)
    hostname = 'https://pubg-esports.gamepedia.com'
    link = 'https://pubg-esports.gamepedia.com/PUBG_Esports_Wiki:Tournaments/'+year
    if CS.check(link) != 0:
        output = open('pubg-esports.gamepedia.json', 'w')
        output.write(json.dumps([None]))
        output.close()

        return -1

    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = list()
    tags = '#mw-content-text > div > div > table > tbody > tr > td > div:nth-child(2)'

    print('data')
    for date in soup.select(tags+' > div'):
        temp = date.text
        if temp == 'UPCOMING' or temp == 'CURRENT' or temp == 'PAST' or temp == year:
            continue
        days = temp.split(' - ')
        start = days[0].split(' ')
        end = days[1].split(' ')
        lists.append({'start': year+con.Short(start[0])+"%02d" % int(start[1]), 'end': year+con.Short(
            end[0])+"%02d" % int(end[1]), 'name': None, 'link': None})

    name_list = soup.select(tags+' > span')
    LinkList = soup.select(tags + ' > a')

    for i in range(0, len(lists)):
        lists[i]['name'] = name_list[i].text
        temp = LinkList[i]['href']
        lists[i]['link'] = hostname+temp
        print(lists[i])

    output = open('pubg-esports.gamepedia.json', 'w')
    output.write(json.dumps(lists))
    output.close()

    return 0


parse()
