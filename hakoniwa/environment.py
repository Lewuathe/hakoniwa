import json
import uuid
from logging import getLogger

import yaml

logger = getLogger(__name__)

from .context import Context
from .state import State


class Environment:
    """
    Environment is a domain defining the state machine each entity is wandering around.
    """

    def __init__(self, states: dict[State]) -> None:
        self.context = Context()
        self.states = states
        self.entities = []

    @classmethod
    def from_yaml(cls, filename: str):
        with open(filename, "r") as file:
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
            logger.info(f"Output from {entity.entity_id}: {out_json}")

            action = int(out_json["action"])
            choice = entity.state.choices[action]
            entity.to_state(self.states[choice["next"]])

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
