import requests
from bs4 import BeautifulSoup
import Month_to_NUM as con
import checkStatus as CS
import datetime
import lol_gamepedia_Extention as LE
import jsonout as JO
regin = ['America', 'Europe', 'Asia', 'International']
year = datetime.datetime.today().year
hostname = 'https://lol.gamepedia.com'
link = 'https://lol.gamepedia.com/Leaguepedia:Tournaments'
tags = '#mw-content-text > div > div > div > div > table > tbody > tr:nth-child(2) > td > div > div'


def parse():

    parse_start = datetime.datetime.today()
    if CS.check(link) != 0:
        JO.output('lol.gamepedia.json', [None])
        return -1
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    lists = list()
    j = i = 0
    for div in soup.select(tags):
        print(str(j)+'. '+regin[j])
        j += 1
        for labels in div.select('div > table > tbody > tr'):
            th = labels.select('th')
            if len(th) == 1:
                print(th[0].text)
                if th[0].text == 'PAST':
                    break
            for label in labels.select('td'):
                if i == 0:
                    date = label.text.split(" ")
                    sdate = datetime.datetime(
                        year, con.Short(date[0]), int(date[1]))
                    if(th == 'UPCOMING' and sdate.date() < datetime.datetime.today().date()):
                        sdate = datetime.datetime(
                            year+1, con.Short(date[0]), int(date[1]))
                        print(sdate < datetime.datetime.today())
                    Edate = None
                    if date[2] == '-' and date[3] != '??':
                        edate = datetime.datetime(
                            year, con.Short(date[3]), int(date[4]))
                        if edate.date() < datetime.datetime.today().date():
                            edate = datetime.datetime(
                                year+1, con.Short(date[3]), int(date[4]))
                        Edate = edate.strftime('%Y%m%d')
                elif i == 1:
                    temLink = hostname + label.a['href']
                    lists.append(
                        {'start': sdate.strftime('%Y%m%d'), 'end': Edate, 'name': label.a.text, 'link': temLink, 'data': LE.parse(temLink)})
                i = 0 if i == 2 else i+1
    print('json output')
    JO.output('lol_gamepedia.json', lists)
    print('lolgamepedia parse time : ' +
          str(datetime.datetime.today()-parse_start))
    return 0
