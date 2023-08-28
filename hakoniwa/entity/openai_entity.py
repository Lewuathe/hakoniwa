from .dynamic_entity import DynamicEntity
import openai

class OpenAIEntity(DynamicEntity):

    def __init__(self, apikey, initial_state):
        openai.api_key = apikey
        super().__init__(initial_state=initial_state, name="OpenAIEntity")

    def in_prompt(self, in_text=None):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {
                    "role": "system",
                    "content": """
        We expect you to take action each time based on the list of possible action and state you are now. You are given some input from the environment at each iteration align with the current state and action you took.
        The information given at each iteration includes current state and list of actions with the identifier of action. It also may contain the text input given from the environment.
        Please give us the ID of action you take and the output you would return to the environment according to the following format.

"""
                },
                {
                    "role": "user", "content": in_text
                }
            ]
        )
        print(chat_completion)
        return ""

    def out_response(self):
        pass