import os
from dataclasses import dataclass


@dataclass
class Context:
    name: str = "default"
