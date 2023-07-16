from unittest import TestCase
from unittest.mock import MagicMock, patch
from webcrawler.usecases.crawler import Crawler
from webcrawler.external.web_site import WebSite
from webcrawler.entities.task import Task
from webcrawler.usecases.worker import Worker
from webcrawler.exceptions.out_of_limit import OutOfLimit as OutOfLimitException


class WorkerTest(TestCase):
    def setUp(self) -> None:
        self._task_q = MagicMock()
        attrs = {
            'get.return_value': Task(0, WebSite('http://example.com')),
        }
        self._task_q.configure_mock(**attrs)
        self._storage = MagicMock()

    @patch.object(Crawler, 'crawl', autospec=True, side_effect=OutOfLimitException)
    def test_run(self, crawl_mock):
        worker = Worker(self._task_q, self._storage)
        worker.run()
        crawl_mock.assert_called_once()
        self._task_q.task_done.assert_called_once()
