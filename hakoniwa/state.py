from dataclasses import dataclass

@dataclass
class State:
    id: int
    name: str
    choices: list[dict]
