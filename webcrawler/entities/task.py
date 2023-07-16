from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class Task:
    priority: int
    data_source: Any = field(compare=False)
