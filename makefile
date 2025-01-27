format:
	@echo "Formatting code..."
	poetry run ruff format src

types:
	@echo "Checking types..."
	poetry run mypy src

run:
	@echo "Running application..."
	poetry run python cli.py api

MIGRATION_NAME := migration_at_$(shell date +%Y%m%d%H%M%S)

generate:
	@echo "Generating migration..."
	poetry run python cli.py migration generate "$(MIGRATION_NAME)"

upgrade:
	@echo "Upgrading database..."
	poetry run python cli.py migration upgrade

downgrade:
	@echo "Downgrading database..."
	poetry run python cli.py migration downgrade

test:
	@echo "Running tests..."
	poetry run pytest -v
