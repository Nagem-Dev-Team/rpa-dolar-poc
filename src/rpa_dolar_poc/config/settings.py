from __future__ import annotations

import os
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """Centralizada em variáveis de ambiente (.env) via pydantic‑settings."""

    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    third_party_log_level: str = Field(default="WARNING", alias="THIRD_PARTY_LOG_LEVEL")


    env: ClassVar[str] = os.getenv("APP_ENV", "dev").lower()


    env_file_map: ClassVar[dict[str, str]] = {
        "dev":  "src/rpa_occ_integra/config/env/dev.env",
        "hml":  "src/rpa_occ_integra/config/env/hml.env",
        "prod": "src/rpa_occ_integra/config/env/prod.env"
    }

    env_file: ClassVar[str] = env_file_map.get(env)

    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    

settings = Settings()
