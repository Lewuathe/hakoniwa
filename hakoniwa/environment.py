import json
import logging
from logging import getLogger

import yaml

from .context import Context
from .state import State


class Environment:
    """
    Environment is a domain defining the state machine each entity is wandering around.
    """

    def __init__(self, states: dict[State], context: Context) -> None:
        self.context = context
        self.states = states
        self.entities = []
        logging_handler = logging.FileHandler(self.context.history_file)
        self.logger = getLogger(__name__)
        self.logger.addHandler(logging_handler)
        self.iteration_count = 0

    @classmethod
    def from_yaml(cls, filename: str, context: Context = Context()):
        with open(filename, "r") as file:
            config = yaml.safe_load(file)
            states = {}
            for state_id, state in config["states"].items():
                states[state_id] = State(state_id, state["name"], state["choices"])
            environment = cls(states, context)
            return environment

    def add_entity(self, entity):
        self.entities.append(entity)

    def next(self):
        for entity in self.entities:
            in_prompt = self._build_prompt(entity.state)
            out_response = entity.in_prompt(in_prompt)

            try:
                out_json = json.loads(out_response)
            except json.JSONDecodeError:
                self.logger.debug("Failed to parse response as JSON")
                continue

            action = int(out_json["action"])
            choice = entity.state.choices[action]
            entity.to_state(self.states[choice["next"]])
            self._emit_log(entity.entity_id, choice)

        self.iteration_count += 1

    def _build_prompt(self, state: State):
        self.logger.debug("build prompt")
        choices = "\n"
        for idx, choice in enumerate(state.choices):
            choices += f"  {idx}: {choice['action']}\n"
        prompt = f"""
        State: {state.name}
        Actions:{choices}
        """

        return prompt

    def _emit_log(self, entity_id: str, choice: dict):
        record = {
            "iteration": self.iteration_count,
            "entity_id": entity_id,
            "action": choice["action"],
            "state": choice["next"],
        }
        self.logger.info(json.dumps(record))
