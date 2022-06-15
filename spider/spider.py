import json
import re
import traceback
from collections import Counter
from urllib.request import Request, urlopen

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
                text, links = self.get_links(new_link)
                ic(links[:5])
                ic(text[500:800])
                self.links.extend(links)
                self.crawled_data[new_link] = text

                text_counter = self.clean_data_and_get_count(text)
                key_value_dict = self.generate_key_value_dict(text_counter, new_link)
                self.update_main_dict(key_value_dict)
                num += 1

    def get_links(self, url):
        """
        This method is used to get all links from a given url.
        """
        text = ""
        links = []
        try:
            req = Request(url)
            html_page = urlopen(req)
            text, links = self.get_links_from_html(html_page)
        except Exception as e:
            traceback.print_exc()
        return text, links

    def get_links_from_html(self, html_content):
        """
        This method is used to get all links from a given html content.
        """
        soup = BeautifulSoup(html_content, "lxml")
        text = soup.get_text()

        links = []
        for link in soup.findAll("a"):
            try:
                split_url_webiste = link.get("href").split("/")[2]
            except:
                continue
            if "utdallas.edu" not in split_url_webiste:
                continue
            links.append(link.get("href"))
        return text, links

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
            key_value_dict[key] = {"count": value, "url": url}
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


if __name__ == "__main__":
    spider = Spider("https://www.utdallas.edu/", 1000)
    spider.crawl()

    # TODO: Add DB
    with open("crawled_data.json", "w") as outfile:
        json.dump(spider.main_key_value, outfile, indent=4)
