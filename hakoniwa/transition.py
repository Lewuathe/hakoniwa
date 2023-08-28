from dataclasses import dataclass
from hakoniwa.action import Action

from hakoniwa.state import State

@dataclass
class Transition:
    from_state: State
    action: Action
    to_state: State
