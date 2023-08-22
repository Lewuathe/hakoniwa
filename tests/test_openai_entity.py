import os

from hakoniwa.entity import OpenAIEntity

def test_entity_in_prompt():
    apikey = os.environ.get("OPENAI_APIKEY", "")
    entity = OpenAIEntity(apikey)
    print(entity.in_prompt())

