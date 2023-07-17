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
            try:
                task = self._queue.get()
                crawler.set_nesting_level(task.priority)
                crawler.crawl(task.data_source)
            except OutOfLimitException as e:
                print(str(e))
                break
            except Exception as e:
                print(str(e))
            finally:
                self._queue.task_done()
