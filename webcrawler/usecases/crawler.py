from ..entities.data_source import DataSource
from ..entities.storage import Storage
from ..entities.tasks_queue import TasksQueue
from ..entities.task import Task
from typing import List
from datetime import datetime


class Crawler:
    def __init__(self, storage: Storage, queue: TasksQueue, nesting_level: int = 0):
        self._storage = storage
        self._queue = queue
        self._nesting_level = nesting_level

    def set_nesting_level(self, nesting_level: int):
        self._nesting_level = nesting_level

    def crawl(self, data_source: DataSource):
        self.save_content(data_source.get_name(), data_source.get_content())
        self.crawl_links(data_source.get_links())

    def save_content(self, name: str, content):
        path = name + '_' + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        self._storage.save_content(content, path)

    def crawl_links(self, links: List[DataSource]):
        for link in links:
            self._queue.push(
                Task(priority=self._nesting_level + 1, data_source=link)
            )
