from logging import getLogger

import openai

from hakoniwa.entity.entity import Entity

logger = getLogger(__name__)


from .dynamic_entity import DynamicEntity


class OpenAIEntity(DynamicEntity):
    def __init__(self, entity_id, apikey, initial_state, personality=None):
        openai.api_key = apikey
        self.personality = personality
        super().__init__(entity_id=entity_id, initial_state=initial_state)

    def in_prompt(self, in_text=""):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {
                    "role": "system",
                    "content": 
                    """
Select the desired action on the list of possible actions based on the your personality and state you are now on.
Please give us the following JSON which has an action ID you took in "action" field, and arbitrary output text in "output" field.

{
  "action": <Action ID>,
  "output": <Output Text>
}
""",
                },
                {"role": "user", "content": f"Personality: {self.personality}, {in_text}"},
            ],
        )

        if len(chat_completion.choices) == 0:
            return "{}"

        response = chat_completion.choices[0].message.content
        return response

    def interact(self, other: Entity):
        in_text = f"""{self.personality}".
        You are in a state '{self.state.name}' with {other.entity_id}. Say something to #{other.entity_id}?
        """
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Provide the response to the other entity.",
                },
                {"role": "user", "content": in_text},
            ],
        )

        if len(chat_completion.choices) == 0:
            return "{}"

        response = chat_completion.choices[0].message.content
        return response
