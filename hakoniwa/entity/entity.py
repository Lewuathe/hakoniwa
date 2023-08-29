from hakoniwa.state import State


class Entity:
    def __init__(self, entity_id: str, initial_state: State) -> None:
        self.state = initial_state
        if entity_id is None:
            self.entity_id = id(self)
        else:
            self.entity_id = entity_id

    def in_prompt(self, in_text=""):
        return "FIXME"
    
    def to_state(self, state):
        self.state = state
