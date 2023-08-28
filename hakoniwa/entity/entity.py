from hakoniwa.state import State


class Entity:
    def __init__(self, initial_state: State, entity_id=None) -> None:
        self.state = initial_state
        if entity_id is None:
            entity_id = id(self)

    def in_prompt(self, in_text=None):
        return "Get input"

    def out_response(self):
        return "Hi, I'm an entity"
    
    def to_state(self, state):
        self.state = state
