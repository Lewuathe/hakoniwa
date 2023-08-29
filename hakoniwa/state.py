from dataclasses import dataclass


@dataclass
class State:
    """
    State is a descrete field where an entity resides at the specific time of the iteration.
    """

    id: int
    name: str
    choices: list[dict]
