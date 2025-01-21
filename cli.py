from typer import Typer, Argument
from enum import Enum
from typing import Annotated
from src.main import run_api_app

cli = Typer(help="Libretto CLI")

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
        


cli()
