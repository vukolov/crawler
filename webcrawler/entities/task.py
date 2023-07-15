from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class Task:
    priority: int
    item: Any = field(compare=False)
