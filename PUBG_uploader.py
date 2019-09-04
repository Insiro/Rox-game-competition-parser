from pymongo import MongoClient
import json
from pprint import pprint


def upload():
    filename = ['pubg_esports_gamepedia.json']
    client = MongoClient()
    client = MongoClient('localhost')
    db = client['rox']
    collection = db['PUBG']
    # number of find data :data.count()
    for fname in filename:
        PUBG = open(fname, 'r').read()
        Jdata = json.loads(PUBG)
        for data in Jdata:
            name = data.get('name')
            print(name)
            trig = {'name': name}
            tet = collection.find(trig)
            if tet.count() == 0:
                print('inset new data')
                collection.insert(data)


if __name__ == "__main__":
    upload()
