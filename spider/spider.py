import json
import os
import re
import traceback
from collections import Counter
from urllib.request import Request, urlopen
from matplotlib.pyplot import title

import nltk
from bs4 import BeautifulSoup
from icecream import ic
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


class Spider:
    """
    This class is used to crawl the web.
    """
    def __init__(self, url, max_urls=10, exceptions=[]):
        self.url = url
        self.max_urls = max_urls
        self.links = []
        self.texts = []
        self.crawled = []
        self.crawled_data = {}
        self.main_key_value = {}
        self.url_data = {}

    def crawl(self):
        """
        This method is used to crawl the web.
        """
        self.links.append(self.url)
        num = 0
        while self.links:
            if num == self.max_urls:
                break
            new_link = self.links.pop()

            if (
                "makeprint" in new_link
                or "makepdf" in new_link
                or "makeword" in new_link
            ):
                continue

            if new_link not in self.crawled:
                self.crawled.append(new_link)
                print(new_link)
                text, links, title = self.get_links(new_link)
                self.links.extend(links)
                self.crawled_data[new_link] = text

                text_counter = self.clean_data_and_get_count(text)
                key_value_dict = self.generate_key_value_dict(text_counter, new_link)
                self.update_main_dict(key_value_dict)
                self.url_data[new_link] = {"title": title, "text": text}
                num += 1

    def get_links(self, url):
        """
        This method is used to get all links from a given url.
        """
        text = ""
        links = []
        title = ""
        try:
            req = Request(url)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            text, links, title = self.get_links_from_html(soup)
        except Exception as e:
            traceback.print_exc()
        return text, links, title

    def get_links_from_html(self, soup):
        """
        This method is used to get all links from a given html content.
        """
        text = soup.get_text()
        title = soup.title.get_text()

        links = []
        for link in soup.findAll("a"):
            try:
                split_url_webiste = link.get("href").split("/")[2]
            except:
                continue
            if "utdallas.edu" not in split_url_webiste:
                continue
            links.append(link.get("href"))
        return text, links, title

    def clean_data_and_get_count(self, text):
        """
        This method is used to clean the crawled data.
        """
        text_tokens = word_tokenize(text)
        tokens_without_sw = [
            word for word in text_tokens if not word in stopwords.words()
        ]
        return Counter(tokens_without_sw)

    def generate_key_value_dict(self, count_dict, url):
        """
        This method is used to generate a key value dict.
        """
        key_value_dict = {}
        for key, value in count_dict.items():
            key_value_dict[key.lower()] = {"count": value, "url": url}
        return key_value_dict

    def update_main_dict(self, key_value_dict):
        """
        This method is used to update the final dict and DB.
        """
        for key, value in key_value_dict.items():
            if key in self.main_key_value:
                self.main_key_value[key].append(value)
            else:
                self.main_key_value[key] = [value]
    
    def get_title(self, soup):
        return soup.title.get_text()


if __name__ == "__main__":
    spider = Spider("https://www.utdallas.edu/", 100)
    save_location = os.path.join("data", "crawled_data_1")
    spider.crawl()

    # TODO: Add DB
    with open(f"{save_location}.json", "w") as outfile:
        json.dump(spider.main_key_value, outfile, indent=4)
    
    with open(f"{save_location}_urls.json", "w") as outfile:
        json.dump(spider.url_data, outfile, indent=4)
