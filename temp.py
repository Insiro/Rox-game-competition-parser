import requests
from bs4 import BeautifulSoup

link = 'https://lol.gamepedia.com/Leaguepedia:Tournaments'
req = requests.get(link)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

print(soup)
#line = soup.find('div',{'class':'content2 separator2 frontpageDynamicSection'})

tags = '#mw-content-text > div > div > div > div > table > tbody > tr:nth-child(2) > td > div > div._toggle.tab-Americas.tabs4 > div:nth-child(2) > table > tbody > tr'
print(soup.select(tags))
##mw-content-text > div > div > div > div > table > tbody > tr:nth-child(2) > td > div

"""
i = 0
j = 0
str2 = ''
for tag in soup.select(tags):
    if i == 0:
        i += 1
        if j != 0:
            str2 += '\n'
        str2 += str(j + 1)
    elif i == 1:
        str2 += ' ' + tag.text[:7] + ' '
        i += 1
    elif i == 4:
        i = 0
        j += 1
        str2 += ''.join(tag.text[4:].split(' '))
    else:
        i += 1
        continue
print(str2)
contents = str2
"""