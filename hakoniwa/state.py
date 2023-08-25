from dataclasses import dataclass

@dataclass
class State:
    id: int
    name: str
    actions: dict