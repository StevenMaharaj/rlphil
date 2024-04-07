from dataclasses import dataclass





@dataclass
class State:
    Sum: int
    Dealer: int
    UsableAce: bool

    def tstr(self) -> str:
        return f"{self.Sum}-{self.Dealer}-{self.UsableAce}"

