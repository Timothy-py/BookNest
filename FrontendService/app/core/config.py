from functools import lru_cache


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(env_file=".env")
    

settings = Settings()


@lru_cache
def get_settings():
    return settings

env_vars = get_settings()