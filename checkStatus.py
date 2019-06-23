import requests


def check(strs):
    temp = requests.get(strs)
    header = temp.status_code
    if header == 200 or header == 201:
        return 0
    else:
        return header
