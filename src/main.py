import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

# from src.config import settings
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

    # app.mount(settings.app.app_mount)

    @app.get("/")
    async def index() -> dict[str, str]:
        return {"message": "check api/v1/docs for docs"}

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None,
    )
