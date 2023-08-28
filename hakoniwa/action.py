from dataclasses import dataclass
from typing import Self

from hakoniwa.environment import Environment

@dataclass
class Action:
    id: int
    name: str

    @classmethod
    def build(name: str, environment: Environment) -> Self:
        return Action(id=environment.next_id(), name=name)