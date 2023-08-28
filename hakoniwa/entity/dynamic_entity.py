from .entity import Entity

class DynamicEntity(Entity):
    """
    A DynamicEntity is an Entity that can create the response at runtime.
    """
    def __init__(self, initial_state, name):
        super().__init__(initial_state=initial_state, entity_id=name)