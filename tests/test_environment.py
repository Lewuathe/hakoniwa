import os
from hakoniwa.entity.openai_entity import OpenAIEntity

from hakoniwa.environment import Environment

def test_environment_in_prompt():
    environment = Environment.from_yaml('./tests/test_env.yaml')
    apikey = os.environ.get("OPENAI_APIKEY", "")
    entity = OpenAIEntity(apikey=apikey, initial_state=environment.states['state0'])
    environment.add_entity(entity)
    environment.next()
    
    # Choose stay inside
    assert entity.state in environment.states.values()







