from abc import ABCMeta, abstractmethod
from typing import List


class DataSource(metaclass=ABCMeta):
    @abstractmethod
    def __int__(self, path):
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def get_content(self):
        ...

    @abstractmethod
    def get_links(self) -> List['DataSource']:
        ...
