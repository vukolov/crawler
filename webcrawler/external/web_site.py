from __future__ import annotations
from ..entities.data_source import DataSource
from typing import List
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from uuid import uuid4


class WebSite(DataSource):
    def __init__(self, path: str):
        self.validate_path(path)
        self._path = path
        self._content = None

    def validate_path(self, path: str):
        #todo: throw an exception if the URL is not valid
        ...

    def get_name(self) -> str:
        name = self._path
        valid_name = re.sub('(http|https)://', '', name)
        valid_name = re.sub('[^a-zA-Z0-9_.-]', '_', valid_name)
        return valid_name + '_' + str(datetime.now().strftime("%H-%M-%S")) + str(uuid4()) + '.html'

    def get_content(self):
        print(f'Getting content from {self._path}...')
        response = requests.get(self._path)
        self._content = response.text
        return self._content

    def get_links(self) -> List['WebSite']:
        links = []
        if self._content:
            soup = BeautifulSoup(self._content, 'html.parser')
            for link in soup.find_all('a'):
                links.append(WebSite(link.get('href')))
        return links
