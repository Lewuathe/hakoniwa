# 箱庭 (Hakoniwa) ![Build](https://github.com/Lewuathe/hakoniwa/actions/workflows/main.yml/badge.svg)

"Hakoniwa" which is a miniature garden in Japanese is a simulation framework letting LLM based entities play around inside. This framework aims to provide the way to experiment how the LLM behaves in the specific domain defined as a simple state machine which has states and actions respectively. The framework is designed to be able to be used for the following purposes:

- To experiment how the LLM behaves in the specific enviroment.
- To collect the behavior data resembling the human behavior in the real world.

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