import os
from dataclasses import dataclass


@dataclass
class Context:
    name: str = "default"
    history_file: str = "history.jsonl"
    need_interaction: bool = True
