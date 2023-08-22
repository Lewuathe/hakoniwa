from .dynamic_entity import DynamicEntity
import openai

class OpenAIEntity(DynamicEntity):

    def __init__(self, apikey):
        openai.api_key = apikey
        super().__init__("OpenAI")

    def in_prompt(self, in_text=None):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": "Hello world"}]
        )
        print("AAA")
        print(chat_completion)
        return ""

    def out_response(self):
        pass