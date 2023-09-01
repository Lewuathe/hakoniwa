from logging import getLogger

import openai

logger = getLogger(__name__)


from .dynamic_entity import DynamicEntity


class OpenAIEntity(DynamicEntity):
    def __init__(self, entity_id, apikey, initial_state, personality=None):
        openai.api_key = apikey
        self.personality = personality
        super().__init__(entity_id=entity_id, initial_state=initial_state)

    def in_prompt(self, in_text=""):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"{self.personality}" + """
We expect you to take action each time based on the list of possible action and state you are now. You are given some input from the environment at each iteration align with the current state and action you took.
Please give us the ID of action you would take and the output text you would return to the environment according to the following JSON format which have an action ID you took in "action" field, and arbitrary output text in "output" field.

{
  "action": <Action ID>,
  "output": <Output Text>
}
""",
                },
                {"role": "user", "content": in_text},
            ],
        )

        if len(chat_completion.choices) == 0:
            return "{}"

        response = chat_completion.choices[0].message.content
        return response
