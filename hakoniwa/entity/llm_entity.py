from .dynamic_entity import DynamicEntity

class LLMEntity(DynamicEntity):
    def __init__(self, name):
        super().__init__(name)