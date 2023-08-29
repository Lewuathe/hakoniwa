init:
	poetry install

test:
	poetry run pytest

lint:
	isort --check --diff hakoniwa tests
	black --check hakoniwa tests

format:
	isort hakoniwa tests
	black hakoniwa tests

.PHONY: init test lint format

