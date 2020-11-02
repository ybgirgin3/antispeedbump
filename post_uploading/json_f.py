import json

def fuck(pic_name, json_file):
    sp = pic_name.split(" ")

    with open(json_file, 'r') as f:
        r = f.read()
        ret = json.loads(r)
        for i in ret[sp[0]]:
            return i



pic1 = "M M6 asd"


ret = fuck(pic_name = pic1, json_file = 'tags.json')
from pprint import pprint
pprint(ret)


