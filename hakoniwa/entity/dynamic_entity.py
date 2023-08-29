from .entity import Entity


class DynamicEntity(Entity):
    """
    A DynamicEntity is an Entity that can create the response at runtime.
    """

    def __init__(self, entity_id, initial_state):
        super().__init__(entity_id=entity_id, initial_state=initial_state)
