
.PHONY: install
install:
	pip install -U poetry && poetry install

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run pre-commit install && poetry run pre-commit run

.PHONY: run-example
run-example:
	poetry run python -m example.main
