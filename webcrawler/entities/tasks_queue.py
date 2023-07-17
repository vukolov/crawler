from queue import PriorityQueue
from .task import Task
from ..exceptions.out_of_limit import OutOfLimit as OutOfLimitException


class TasksQueue:
    def __init__(self, max_tasks: int):
        self._queue = PriorityQueue()
        self._max_tasks = max_tasks
        self._tasks_counter = 0

    def push(self, task: Task):
        self._queue.put(task)

    def get(self):
        return self._queue.get(block=True)

    def check_tasks_limit(self):
        if self._tasks_counter >= self._max_tasks:
            raise OutOfLimitException('Max depth has been reached. Exiting thread...')

    def increase_processed_task_counter(self, amount: int = 1):
        self._tasks_counter += amount

    def task_done(self):
        self._queue.task_done()
