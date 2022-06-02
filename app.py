from flask import Flask, request

from controllers.webpages import Webpage

app = Flask(__name__)

@app.route('/webpage', methods=['GET'])
def get_webpage():
    webpage = Webpage()
    args = request.args
    name = args.get("name")
    return webpage.get_webpage(name)
    

if __name__ == "__main__":
    app.run(debug=True)