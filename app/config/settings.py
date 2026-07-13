from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    openai_api_key: str = ""

    anthropic_api_key: str = ""

    openai_model: str = "gpt-4o"

    max_iterations: int = 10

    request_timeout: int = 30

    debug: bool = True
    gemini_api_key: str = ""

@lru_cache
def get_settings() -> Settings:
    return Settings()