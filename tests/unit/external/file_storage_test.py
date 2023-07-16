from unittest import TestCase
from unittest.mock import patch, mock_open
from webcrawler.external.file_storage import FileStorage


class FileStorageTest(TestCase):
    def setUp(self):
        self._file = None

    @patch('pathlib.Path.mkdir')
    @patch('builtins.open', new_callable=mock_open())
    def test_save_content(self, mock_file, mock_mkdir):
        content = '<html></html>'
        file_storage = FileStorage('storage/')
        file_storage.save_content(content, 'test_file.html')
        mock_file.assert_called_with('storage/test_file.html', 'w')
        mock_file.return_value.__enter__().write.assert_called_once_with(content)
        mock_mkdir.assert_called_with(parents=True, exist_ok=True)
