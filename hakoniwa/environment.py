import uuid
import yaml
import json
from logging import getLogger
logger = getLogger(__name__)

from .context import Context
from .state import State

class Environment:
    def __init__(self, states: dict[State]) -> None:
        self.context = Context()
        self.states = states
        self.entities = []

    def next_id(self) -> str:
        return str(uuid.uuid4())
    
    @classmethod
    def from_yaml(cls, filename: str):
        with open(filename, 'r') as file:
            config = yaml.safe_load(file)
            states = {}
            for state_id, state in config["states"].items():
                states[state_id] = State(state_id, state["name"], state["choices"])
            environment = cls(states)
            return environment
        
    def add_entity(self, entity):
        self.entities.append(entity)

    def next(self):
        for entity in self.entities:
            in_prompt = self._build_prompt(entity.state)
            out_response = entity.in_prompt(in_prompt)
            out_json = json.loads(out_response)
            logger.info(f"out_json: {out_json}")

            logger.info(f"entity.state: {entity.state}")

            action = int(out_json['action'])
            choice = entity.state.choices[action]
            entity.state = self.states[choice['next']]

    def _build_prompt(self, state: State):
        choices = ""
        for idx, choice in enumerate(state.choices):
            choices += f"  {idx}: {choice['action']}\n"
        prompt = f"""
        State: {state.name}
        Actions:
        {choices}
        """

        return prompt

