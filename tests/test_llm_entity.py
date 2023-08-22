from hakoniwa.entity import LLMEntity

def test_entity_in_prompt():
    entity = LLMEntity("test")
    assert entity.in_prompt() == "Get input"

def test_entity_out_prompt():
    entity = LLMEntity("test")
    assert entity.out_prompt() == "Hi, I'm an entity"    