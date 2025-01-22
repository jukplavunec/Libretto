from dynaconf import Dynaconf
from pydantic import BaseModel

settings = Dynaconf(
    envvar_prefix="APP",
    settings_files=["settings.toml", ".secrets.toml"],
)


class DBConfig(BaseModel):
    db_user: str
    db_password: str
    db_host: str
    db_name: str
    db_port: int

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    

class APPConfig(BaseModel):
    app_name: str
    app_port: int
    app_host: str
    app_version: str
    app_mount: str


class Settings(BaseModel):
    app: APPConfig
    db: DBConfig


dyna_settings = Dynaconf(
    envvar_prefix="APP",
    settings_files=["settings.toml"],
)

settings = Settings(
    app=dyna_settings["app_settings"],
    db=dyna_settings["db_settings"],
)
