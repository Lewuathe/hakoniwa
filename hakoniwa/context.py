import os

from dataclasses import dataclass

@dataclass
class Context:
    name: str = "default"
    openai_apikey: str = os.environ.get("OPENAI_APIKEY", "")
