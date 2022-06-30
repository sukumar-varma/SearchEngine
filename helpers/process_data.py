import json
import os


with open('crawled_data.json', 'r') as f:
    data = json.load(f)
alphabet =  {k.lower(): v for k, v in data.items()}
# print(alphabet.keys())

with open("new_crawled_data.json", "w") as f:
    json.dump(alphabet, f, indent=4)
