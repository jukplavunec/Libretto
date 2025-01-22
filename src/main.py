import uvicorn
from fastapi import FastAPI

from src.config import settings
from src.app import get_app
from src.logger import configure_logger


def run_api_app() -> None:
    configure_logger(
        enable_json_logs=False,
        enable_sql_logs=True,
        level=10,
    )
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
    )

    app.mount(settings.app.app_mount, get_app())

    @app.get("/")
    async def index() -> dict[str, str]:
        return {"message": "check api/v1/docs for docs"}

    uvicorn.run(
        app,
        host=settings.app.app_host,
        port=settings.app.app_port,
        log_config=None,
    )
