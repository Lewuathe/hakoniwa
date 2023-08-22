class Entity:
    def __init__(self, entity_id=None) -> None:
        if entity_id is None:
            entity_id = id(self)

    def in_prompt(self, in_text=None):
        return "Get input"

    def out_response(self):
        return "Hi, I'm an entity"