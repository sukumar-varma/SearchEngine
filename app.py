import time

from flask import Flask, request, jsonify, render_template
from icecream import ic
from controllers.webpages import Webpage

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/webpage', methods=['GET'])
def get_webpage():
    webpage = Webpage()
    args = request.args
    name = args.get("name")
    return jsonify(webpage.get_webpage(name))

@app.route('/search', methods=['POST'])
def search():
    webpage = Webpage()
    if request.method == 'POST':
        start = time.process_time()
        words = request.form['search_box'].strip().lower().split(" ")

        links = webpage.get_webpage(words[0])
        for word in words[1:]:
            links.extend(webpage.get_webpage(word))
        
        links = [i for n, i in enumerate(links) if i not in links[n + 1:]]
        return render_template('results.html', links=links, links_count=len(links), time_taken=time.process_time() - start)


if __name__ == "__main__":
    app.run(debug=True)
