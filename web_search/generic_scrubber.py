from abc import ABC

from bs4 import BeautifulSoup


class GenericScrubber(ABC):
    def __init__(self, web_data: str):
        self.soup = BeautifulSoup(web_data)

    def set_new_soup(self, new_soup):
        self.soup = BeautifulSoup(new_soup)
