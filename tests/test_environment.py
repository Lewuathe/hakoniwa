import os
from hakoniwa.entity.openai_entity import OpenAIEntity

from hakoniwa.environment import Environment

def test_environment_in_prompt():
    with open('tests/test_env.yaml', 'r') as file:
        environment = Environment.from_yaml('./tests/test_env.yaml')

        apikey = os.environ.get("OPENAI_APIKEY", "")
        entity = OpenAIEntity(apikey=apikey, initial_state=environment.states[0])

        environment.add_entity(entity)

        environment.next()







