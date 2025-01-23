from typer import Typer, Argument
from enum import Enum
from typing import Annotated
from src.main import run_api_app
import subprocess

cli = Typer(help="Libretto CLI")
migration = Typer(help="Migration commands")
cli.add_typer(migration, name="migration")

class Apps(str, Enum):
    api = "api"
    background_task = "background_task"

@cli.command(help="Run the application")
def main(
    app: Annotated[Apps, Argument(help="The application to run")] = Apps.api
):
    match app:
        case Apps.api:
            run_api_app()
        case Apps.background_task:
            print("Running background task")
        

@migration.command(help="Autogenerate python and sql migration")
def generate(
    name: Annotated[str, Argument(help="Migration name")]
):
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", name], check=True)
    print(f"{name} migration generated seccessfully")


@migration.command(help="Apply all migrations")
def upgrade():
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    print("All migrations applied successfully.")

@migration.command(help="Revert last migration")
def downgrade():
    subprocess.run(["alembic", "downgrade", "-1"], check=True)
    print("Last migration reverted successfully.")

cli()
