# pubg-esports.gamepedia.com
from bs4 import BeautifulSoup
import requests


link = 'https://pubg-esports.gamepedia.com/PUBG_Esports_Wiki:Tournaments/2019'
req = requests.get(link)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
lists = list()
tags = '#mw-content-text > div > div > table > tbody > tr > td > div:nth-child(2)'

now = soup.select(tags)
for asd in now[0].text.split('<br/>'):
    print(asd)
