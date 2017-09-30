"""Classe de base Phone"""
import requests


# import xml.etree.ElementTree as ET


class Phone(object):
    def __init__(self):
        self.battery_level = None
        self.network_ok = True
        self.last_news = None

    def workfor(self, seconds):
        raise NotImplementedError

    def chargefor(self, seconds):
        raise NotImplementedError

    def _real_get_news(self):
        return requests.get("https://www.yahoo.com/news/rss/entertainment")\
            .text

    def show_news(self):
        if self.last_news is not None:
            return self.last_news
        if self.network_ok:
            str = self._real_get_news()
            # print('str',str)
            # tree = ET.fromstring(str)
            self.last_news = str
        return self.last_news
