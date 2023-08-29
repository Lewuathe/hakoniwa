import os

import pytest

from hakoniwa.entity import HelloEntity
from hakoniwa.entity.openai_entity import OpenAIEntity
from hakoniwa.environment import Environment


def test_environment_build():
    environment = Environment.from_yaml("./tests/test_env.yaml")
    assert environment is not None


def test_environment_states():
    environment = Environment.from_yaml("./tests/test_env.yaml")
    assert len(environment.states) == 3


def test_add_entity():
    environment = Environment.from_yaml("./tests/test_env.yaml")
    environment.add_entity(HelloEntity(entity_id="test", initial_state=environment.states["state0"]))
    assert len(environment.entities) == 1


def test_iteration():
    environment = Environment.from_yaml("./tests/test_env.yaml")
    entity = HelloEntity(entity_id="test", initial_state=environment.states["state0"])
    environment.add_entity(entity=entity)
    environment.next()
    assert entity.state == environment.states["state1"]


@pytest.mark.skipif("OPENAI_APIKEY" not in os.environ, reason="requires OPENAI_APIKEY")
def test_environment_in_prompt():
    environment = Environment.from_yaml("./tests/test_env.yaml")
    apikey = os.environ.get("OPENAI_APIKEY", "")
    entity = OpenAIEntity(entity_id="OpenAI1", apikey=apikey, initial_state=environment.states["state0"])
    environment.add_entity(entity)
    environment.next()

    # Choose stay inside
    assert entity.state in environment.states.values()
