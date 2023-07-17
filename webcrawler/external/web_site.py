from __future__ import annotations
from ..entities.data_source import DataSource
from typing import List
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from uuid import uuid4


class WebSite(DataSource):
    def __init__(self, url: str):
        self._url = url
        self._content = None

    def get_name(self, prefix: str = '') -> str:
        return prefix + str(datetime.now().strftime("%H-%M-%S")) + '_' + str(uuid4()) + '.html'

    def get_content(self):
        print(f'Getting content from {self._url}...')
        response = requests.get(self._url)
        self._content = response.text
        return self._content

    def get_links(self) -> List['WebSite']:
        links = []
        if self._content:
            soup = BeautifulSoup(self._content, 'html.parser')
            for link in soup.find_all('a'):
                links.append(WebSite(link.get('href')))
        return links
