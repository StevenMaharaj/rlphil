from dataclasses import dataclass, field
from typing import List

from state import State



@dataclass
class Episode:
    S:List[State] = field(default_factory=list)
    A:List[int] = field(default_factory=list)
    R:List[float] = field(default_factory=list)



