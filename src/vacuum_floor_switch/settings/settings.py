from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    token: str
    ip: str
    device_id: int
    lower_floor_id: int
    upper_floor_id: int


@lru_cache
def get_settings():
    return Settings()
