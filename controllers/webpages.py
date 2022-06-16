import json
from flask import jsonify

class Webpage:
    def __init__(self):
        pass
    
    def get_webpage(self, name):
        arr = []
        with open('crawled_data.json', 'r') as f:
            data = json.load(f)
            for i in data[name]:
                arr.append(i['url'])
        return jsonify(arr)