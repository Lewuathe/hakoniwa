from hakoniwa.entity import HelloEntity


def test_hello():
    entity = HelloEntity(entity_id="test", initial_state=None)
    assert entity.in_prompt() == '{"action": 0, "output": "Hello World!"}'
