import requests
from bs4 import BeautifulSoup
import checkStatus as CS
import jsonout

link = 'overwatchleague'
tag = '#schedule > div > div.Background.u-bottomPadding--large.u-topPadding--medium > div > div > div:nth-child(1) > div.MatchRow-header.MatchRow.Date.Date--reverse'