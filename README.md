# 箱庭 (Hakoniwa) ![Build](https://github.com/Lewuathe/hakoniwa/actions/workflows/main.yml/badge.svg)

"Hakoniwa" which is a miniature garden in Japanese is a simulation framework letting LLM based entities play around inside. This framework aims to provide the way to experiment how the LLM behaves in the specific domain defined as a simple state machine which has states and actions respectively. The framework is designed to be able to be used for the following purposes:

- To experiment how the LLM behaves in the specific enviroment.
- To collect the behavior data resembling the human behavior in the real world.

## Usage

### Define the state machine
First of all, we can define the state machine where each agent play around inside. The state machine is defined as a YAML file. The following is the example of the state machine definition.

```yaml
states:
  state0:
    name: In the house
    choices:
      - action: Go outside
        next: state1
      - action: Stay inside
        next: state0
  state1:
    name: Outside
    choices:
      - action: Go to the supermarket
        next: state2
      - action: Go back home
        next: state0
  state2:
    name: In the supermarket
    choices:
      - action: Go back home
        next: state0

entities:
  - name: OpenAI
    type: openai
    initial_state: state0
```

The state machine consists of the following two parts.
- `states`: The list of states in the state machine. `choices` is the list of actions which the agent can take from the state.
- `entities`: The list of entities which play around inside the state machine.


## Dependencies

Install [Poetry](https://python-poetry.org/) and run the following command to install dependencies.

```
$ poetry install
```

## Development

We can run the unit test with pytest.

```
$ make test
```
