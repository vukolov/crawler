from ..entities.data_source import DataSource
from ..entities.storage import Storage
from ..entities.tasks_queue import TasksQueue
from ..entities.task import Task
from typing import List


class Crawler:
    def __init__(self, storage: Storage, queue: TasksQueue, nesting_level: int = 0):
        self._storage = storage
        self._queue = queue
        self._nesting_level = nesting_level

    def set_nesting_level(self, nesting_level: int):
        self._nesting_level = nesting_level

    def crawl(self, data_source: DataSource):
        content = data_source.get_content()
        if content:
            self._queue.check_tasks_limit()
            self._queue.increase_processed_task_counter()
            self.save_content(data_source.get_name(), content)
            self.crawl_links(data_source.get_links())

    def save_content(self, name: str, content):
        self._storage.save_content(content, name)

    def crawl_links(self, links: List[DataSource]):
        nesting_level = self._nesting_level + 1
        for link in links:
            self._queue.push(
                Task(priority=nesting_level, data_source=link)
            )
