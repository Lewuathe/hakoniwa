import json
import logging
from logging import getLogger

import yaml

from hakoniwa.entity.entity import Entity

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
            context.need_interaction = config["context"]["need_interaction"]
            environment = cls(states, context)
            return environment

    def add_entity(self, entity):
        self.entities.append(entity)

    def next(self):
        for entity in self.entities:
            in_prompt = self._build_prompt(entity)
            out_response = entity.in_prompt(in_prompt)

            try:
                out_json = json.loads(out_response)
            except json.JSONDecodeError:
                self.logger.debug("Failed to parse response as JSON")
                return

            action = int(out_json["action"])
            choice = entity.state.choices[action]
            entity.to_state(self.states[choice["next"]])
            self._emit_log(entity.entity_id, choice, in_prompt)

        self.iteration_count += 1

    def _build_prompt(self, entity: Entity):
        state = entity.state
        choices = "\n"
        action_id = 0
        for _, choice in enumerate(state.choices):
            choices += f"  {action_id}: {choice['action']}\n"
            action_id += 1
        interections = ""
        for other in self.entities:
            if other.entity_id != entity.entity_id and other.state == state and self.context.need_interaction:
                self.logger.debug("Found other entity in the same state")
                interaction = other.interact(entity)
                interections += f"{other.entity_id} says '{interaction}'."
        prompt = f"""
        Context: You are in a state '{state.name}'. {interections}
        Actions:{choices}
        """

        self.logger.debug(prompt)

        return prompt

    def _build_interact_prompt(self, entity: Entity, other: Entity):
        prompt = f"""
        Context: You are in a state {entity.state} with {other.entity_id}. Do you want to say something to #{other.entity_id}?
        """

        return prompt

    def _emit_log(self, entity_id: str, choice: dict, prompt: str):
        record = {
            "iteration": self.iteration_count,
            "entity_id": entity_id,
            "action": choice["action"],
            "state": choice["next"],
            "prompt": prompt,
        }
        self.logger.info(json.dumps(record))
