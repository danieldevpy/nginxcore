from dataclasses import dataclass
from typing import List


@dataclass
class Command:
    name: str
    args: List[str]
    check: bool = True