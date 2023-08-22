from hakoniwa.entity import Entity

def test_entity_in_prompt():
    entity = Entity()
    assert entity.in_prompt() == "Get input"

def test_entity_out_prompt():
    entity = Entity()
    assert entity.out_response() == "Hi, I'm an entity"    