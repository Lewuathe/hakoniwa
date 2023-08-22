from .entity import Entity

class DynamicEntity(Entity):
    def __init__(self, name):
        self.name = name