from hakoniwa.entity.entity import Entity
from hakoniwa.state import State


class HelloEntity(Entity):
    """
    Entity always saying 'Hello World!'
    """

    def __init__(self, entity_id: str, initial_state: State) -> None:
        super().__init__(entity_id, initial_state)

    def in_prompt(self, in_text=""):
        return '{"action": 0, "output": "Hello World!"}'
