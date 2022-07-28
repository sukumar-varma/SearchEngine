import os
import json

from flask import jsonify

class Webpage:
    def __init__(self):
        pass
    
    def get_webpage(self, name):
        arr = []
        with open(os.path.join('data', 'crawled_data_1.json'), 'r') as f:
            with open(os.path.join('data', 'crawled_data_1_urls.json'), 'r') as f_urls:
                data = json.load(f)
                data_urls = json.load(f_urls)
                print(name)
                if name in data:
                    for i in data[name]:
                        # print(data_urls[i["url"]])
                        # print(i['url'])
                        arr.append({"title": data_urls[i["url"]]["title"], "url": i['url'], "text": data_urls[i["url"]]["text"].replace("\n", " ")[:200] + "..."})
        return arr