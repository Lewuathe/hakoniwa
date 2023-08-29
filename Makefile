init:
	poetry install

test:
	poetry run pytest

lint:
	isort --check --diff hakoniwa
	black --check hakoniwa

format:
	isort hakoniwa
	black hakoniwa

.PHONY: init test lint format

