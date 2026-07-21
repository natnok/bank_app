from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = "bank"
    app_version: str = "v1.001.a"

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_reload: bool = True

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
