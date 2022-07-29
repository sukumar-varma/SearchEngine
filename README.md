# UTD Search Engine

A demo is available at [utd-search-engine.herokuapp.com](https://utd-search-engine.herokuapp.com/)

## Getting Started
0. Clone/Fork SearchEngine repo:

    `git clone https://github.com/vdasari98/SearchEngine.git`
    create a new branch
    Happy coding!

### Windows setup:
1. Install python
    www.python.org --> Downloads --> Download and install Python 3.9.1

2. Install pip
    `py get-pip.py`

3. Install virtualenv
    `pip install virtualenv`

4. Creating virtualenv
    `virtual env`

5. Activate env
    `.\env\Scripts\activate`

6. Install requirements
    `pip install requirements.txt`

7. Spinning up server
    python app.py

### Linux/macos setup:
1. Install python
    www.python.org --> Downloads --> Download and install Python 3.9.1

2. Install pip
    `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
    `python3 get-pip.py`

3. Install virtualenv
    `pip install python-venv`

4. Creating virtualenv
    `python -m venv venv`

5. Activate env
    `./venv/bin/activate`

6. Install requirements
    `pip install requirements.txt`

7. Spinning up server
    python app.py


## Project Structure

```bash
.
├── Procfile
├── README.md
├── __pycache__
│   ├── app.cpython-39.pyc
│   └── wsgi.cpython-39.pyc
├── app.py
├── controllers
│   ├── __pycache__
│   │   └── webpages.cpython-39.pyc
│   └── webpages.py
├── data
│   ├── crawled_data_1.json
│   └── crawled_data_1_urls.json
├── docs
│   ├── Final_PPT.pptx
│   ├── interim_project_1.pptx
│   └── ~$Final_PPT.pptx
├── helpers
│   ├── process_data.py
│   └── setup_db.py
├── requirements.txt
├── runtime.txt
├── spider
│   └── spider.py
├── templates
│   ├── index.html
│   └── results.html
└── wsgi.py
```

## Web Spider:

To start the web spider/crawler, run `python spider/spider.py`. JSON data will be generated in `./data/crawled_data.json`

## Start server

To start the server run `python app.py`

The app runs on the follow URL: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Deployment

You can directly deploy to heroku using pushing to heroku remote:
`git push heroku master`

`heroku open` then opens the url or by visiting (https://utd-search-engine.herokuapp.com/)[https://utd-search-engine.herokuapp.com/]

## Changelog
`v2.0`: Results page now displays title and description. Improved query speed.

`v1.1`: Added more functionality to crawler to get titles and descirptions

`v1.0`: Added auto suggestions to suggest keywords as they are typed. More refined user interface for search and results page

`v0.2`: Added multi keyword search

`v0.1`: Written crawler to crawl through a domain and get URLs and content. Provided a simple UI using flask templates to search and display search results

