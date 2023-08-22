from .context import Context

class Environment:
    def __init__(self) -> None:
        self.context = Context()
        self.entities = []