from threading import Thread
from webcrawler.usecases.crawler import Crawler
from webcrawler.entities.storage import Storage
from webcrawler.entities.tasks_queue import TasksQueue
from webcrawler.exceptions.out_of_limit import OutOfLimit as OutOfLimitException


class Worker(Thread):
    def __init__(self, queue: TasksQueue, storage: Storage):
        Thread.__init__(self)
        self._queue = queue
        self._storage = storage

    def run(self):
        crawler = Crawler(self._storage, self._queue)
        while True:
            task = self._queue.get()
            try:
                crawler.crawl(task.item)
            except OutOfLimitException as e:
                break
            except Exception as e:
                ...
            finally:
                self._queue.task_done()
