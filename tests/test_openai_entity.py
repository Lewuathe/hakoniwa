import os


from hakoniwa.entity import OpenAIEntity
from hakoniwa.state import State

def test_entity_in_prompt():
    state = State(id=0, name="initial", choices=[])
    apikey = os.environ.get("OPENAI_APIKEY", "")
    entity = OpenAIEntity(entity_id="test", apikey=apikey, initial_state=state)

    response = entity.in_prompt()
    assert "action" in response
    assert "output" in response

