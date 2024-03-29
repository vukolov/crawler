from typing import List
from webcrawler.entities.task import Task
from webcrawler.entities.tasks_queue import TasksQueue
from webcrawler.entities.data_source import DataSource
from webcrawler.entities.storage import Storage
from webcrawler.usecases.worker import Worker
from webcrawler.exceptions.out_of_limit import OutOfLimit as OutOfLimitException
from time import sleep


class App:
    def __init__(self, workers_count: int, data_sources: List[DataSource], storage: Storage, max_tasks: int):
        self._threads = []
        self._workers_count = workers_count
        self._queue = TasksQueue(max_tasks)
        self._data_sources = data_sources
        self._storage = storage

    def run(self):
        for source in self._data_sources:
            self._queue.push(Task(priority=0, data_source=source))
        self._init_threads(self._workers_count)
        self._start_threads()
        while len(self._threads):
            self._check_threads_status()
            sleep(1)

    def _check_threads_status(self):
        for i, thread in enumerate(self._threads):
            if not thread.is_alive():
                self._threads.pop(i)

    def _init_threads(self, workers: int):
        for thread_id in range(workers):
            worker_thread = Worker(self._queue, self._storage)
            self._threads.append(worker_thread)

    def _start_threads(self):
        for thread in self._threads:
            thread.setDaemon(True)
            thread.start()
        print(f'{len(self._threads)} threads have been started')
