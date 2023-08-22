from .entity import Entity

class DynamicEntity(Entity):
    """
    A DynamicEntity is an Entity that can create the response at runtime.
    """
    def __init__(self, name):
        self.name = name