run = poetry run

init:
	poetry install

test:
	poetry run pytest

lint:
	$(run) isort --check --diff hakoniwa tests
	$(run) black --check hakoniwa tests

format:
	$(run) isort hakoniwa tests
	$(run) black hakoniwa tests

.PHONY: init test lint format

