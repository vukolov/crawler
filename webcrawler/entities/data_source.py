from abc import ABCMeta, abstractmethod
from typing import List


class DataSource(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, path):
        ...

    @abstractmethod
    def get_name(self, prefix: str = '') -> str:
        ...

    @abstractmethod
    def get_content(self):
        ...

    @abstractmethod
    def get_links(self) -> List['DataSource']:
        ...
