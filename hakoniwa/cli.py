import logging
import os
from argparse import ArgumentParser

import yaml

from hakoniwa.context import Context
from hakoniwa.entity import OpenAIEntity
from hakoniwa.environment import Environment


def build_environment(args):
    context = Context(args.history_file)
    environment = Environment.from_yaml(filename=args.env_file, context=context)
    with open(args.env_file, "r") as file:
        config = yaml.safe_load(file)
        for entity in config["entities"]:
            if entity["type"] == "openai":
                if "OPENAI_APIKEY" not in os.environ:
                    raise RuntimeError("OpenAI entity is not supported yet")
                environment.add_entity(
                    OpenAIEntity(
                        entity_id=entity["name"],
                        apikey=os.environ["OPENAI_APIKEY"],
                        initial_state=environment.states[entity["initial_state"]],
                        personality=entity["personality"],
                    )
                )
            else:
                raise RuntimeError("Unsupported entity type: {}".format(entity["type"]))

    return environment


def run_iterations(environment, max_iterations):
    for i in range(0, max_iterations):
        environment.next()


def run():
    parser = ArgumentParser(description="Hakoniwa CLI")
    parser.add_argument("-f", dest="env_file", help="File defining the environment")
    parser.add_argument("--iteration", dest="max_iterations", type=int, default=10, help="Max iterations")
    parser.add_argument("--history", dest="history_file", default="history.jsonl", help="History file")

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    environment = build_environment(args)
    run_iterations(environment, args.max_iterations)
