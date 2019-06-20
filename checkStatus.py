import requests


def check(strs):
    header = requests.get(str).status_code
    if header == 404:
        return 404
    else:
        return 0
