from pymongo import MongoClient
import json
from pprint import pprint


def upload():
    filename = ['wcs_starcraft.json']
    client = MongoClient()
    client = MongoClient('localhost')
    db = client['rox']
    collection = db['STARCRAFT']
    # number of find data :data.count()
    for fname in filename:
        st = open(fname, 'r').read()
        Jdata = json.loads(st)
        for data in Jdata:
            name = data.get('name')
            trig = {'name': name}
            tet = collection.find(trig)
            if tet.count() == 0:
                print(name)
                print('inset new data')
                collection.insert(data)


if __name__ == "__main__":
    upload()
