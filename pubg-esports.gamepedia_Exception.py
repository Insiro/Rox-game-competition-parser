import requests
from bs4 import BeautifulSoup
import Month_to_NUM as con
import checkStatus as CS


def parse(link):
    status = CS.check(link)
    if status != 0:
        return status
    