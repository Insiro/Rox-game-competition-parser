import json


def output(filename, data):
    output = open(filename, 'w')
    output.write(json.dumps(data))
    output.close
