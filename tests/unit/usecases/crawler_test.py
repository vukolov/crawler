from unittest import TestCase
from unittest.mock import MagicMock
from webcrawler.usecases.crawler import Crawler
from webcrawler.external.web_site import WebSite
from webcrawler.entities.task import Task


class CrawlerTest(TestCase):
    def setUp(self) -> None:
        self._task_q = MagicMock()
        attrs = {}
        self._task_q.configure_mock(**attrs)
        self._storage = MagicMock()
        attrs = {
            'save_content.return_value': None
        }
        self._storage.configure_mock(**attrs)
        self._nesting_level = 0
        self._crawler = Crawler(
            storage=self._storage,
            queue=self._task_q,
            nesting_level=self._nesting_level
        )

    def test_save_content(self):
        self._crawler._save_content('test_name', '<html></html>')
        self._storage.save_content.assert_called_once()

    def test_crawl_links(self):
        links = [
            WebSite('http://example.com'),
            WebSite('https://google.com'),
        ]
        self._crawler._crawl_links(links)
        self._task_q.push.assert_called_with(Task(self._nesting_level + 1, links[0]))
        self._task_q.push.assert_called_with(Task(self._nesting_level + 1, links[1]))
