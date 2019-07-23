from pymongo import MongoClient
import json
from pprint import pprint


def upload():
    filename = ['toornamentOW.json']
    client = MongoClient()
    client = MongoClient('localhost')
    db = client['rox']
    collection = db['OW']
    # number of find data :data.count()
    for fname in filename:
        OW = open(fname, 'r').read()
        Jdata = json.loads(OW)
        for data in Jdata:
            name = data.get('name')
            print(name)
            trig = {'name': name}
            tet = collection.find(trig)
            if tet.count() == 0:
                print('inset new data')
                collection.insert(data)
