init:
	poetry install

test:
	poetry run pytest

.PHONY: init test