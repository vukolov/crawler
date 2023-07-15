# from __future__ import annotations
from ..entities.data_source import DataSource
from typing import List
import requests
from bs4 import BeautifulSoup


class WebSite(DataSource):
    def __int__(self, path):
        self._path = path
        self._content = None

    def get_name(self) -> str:
        return self._path

    def get_content(self):
        response = requests.get(self._path)
        return response.text

    def get_links(self) -> List['WebSite']:
        links = []
        if self._content:
            soup = BeautifulSoup(self._content, 'html.parser')
            for link in soup.find_all('a'):
                links.append(WebSite(link.get('href')))
        return links
