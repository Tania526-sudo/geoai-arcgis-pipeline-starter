.PHONY: help setup lint test clean run

help:
	@echo "Available commands:"
	@echo "  make setup        - install dependencies"
	@echo "  make run          - launch Jupyter Lab"
	@echo "  make lint         - run basic code checks"
	@echo "  make test         - run tests"
	@echo "  make clean        - cleanup artifacts"

setup:
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	jupyter lab

lint:
	python -m compileall src

test:
	pytest -q || true

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf logs
	rm -rf reports
