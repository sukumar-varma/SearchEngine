import os
import json

from flask import jsonify

class Webpage:
    def __init__(self):
        pass
    
    def get_webpage(self, name):
        arr = []
        with open(os.path.join('data', 'crawled_data.json'), 'r') as f:
            data = json.load(f)
            if name in data:
                for i in data[name]:
                    arr.append(i['url'])
        return arr