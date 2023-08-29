import os

import pytest

from hakoniwa.entity import OpenAIEntity
from hakoniwa.state import State


@pytest.mark.skipif("OPENAI_APIKEY" not in os.environ, reason="requires OPENAI_APIKEY")
def test_entity_in_prompt():
    state = State(id=0, name="initial", choices=[])
    apikey = os.environ.get("OPENAI_APIKEY", "")
    entity = OpenAIEntity(entity_id="test", apikey=apikey, initial_state=state)

    response = entity.in_prompt()
    assert "action" in response
    assert "output" in response
