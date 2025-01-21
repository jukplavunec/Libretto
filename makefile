format:
	@echo "Formatting code..."
	poetry run ruff format src

types:
	@echo "Checking types..."
	poetry run mypy src

run:
	@echo "Running application..."
	poetry run python cli.py api
