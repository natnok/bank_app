from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "bank"
    app_version: str = "v1.001.a"

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_reload: bool = True


settings = Settings()
