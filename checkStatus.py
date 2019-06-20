import requests


def check(strs):
    temp = requests.get(strs)
    header = temp.status_code
    if header == 404:
        return 404
    else:
        return 0
