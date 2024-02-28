from pydantic_settings import BaseSettings, SettingsConfigDict
import os

current_directory = os.getcwd()
DOTNEV = os.path.join(os.path.dirname(current_directory), ".env")
print(DOTNEV)


class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=('.env.'))


settings = Settings()
