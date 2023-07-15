import logging
from typing import List
from webcrawler.entities.task import Task
from webcrawler.entities.tasks_queue import TasksQueue
from webcrawler.entities.data_source import DataSource
from webcrawler.entities.storage import Storage
from webcrawler.usecases.worker import Worker
from webcrawler.exceptions.out_of_limit import OutOfLimit as OutOfLimitException


class App:
    def __int__(self, workers_count: int, data_sources: List[DataSource], storage: Storage, max_tasks: int):
        self._threads = []
        self._workers_count = workers_count
        self._queue = TasksQueue(max_tasks)
        self._data_sources = data_sources
        self._storage = storage

    def run(self):
        for source in self._data_sources:
            try:
                self._queue.push(Task(priority=0, item=source))
            except OutOfLimitException:
                break
        self.init_threads(self._workers_count)
        self.start_threads()

    def init_threads(self, workers: int):
        for thread_id in range(workers):
            worker_thread = Worker(self._queue, self._storage)
            self._threads.append(worker_thread)

    def start_threads(self):
        for thread in self._threads:
            thread.setDaemon(True)
            thread.start()
        logging.info('Threads have been started', {'tag': 'operation'})
