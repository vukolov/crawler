from ..entities.storage import Storage
from pathlib import Path


class FileStorage(Storage):
    def __init__(self, root_path: str):
        self._root_path = root_path
        Path(root_path).mkdir(parents=True, exist_ok=True)

    def save_content(self, content, path: str):
        with open(self._root_path + path, 'w') as file:
            file.write(content)
