"""Configurações de serviço."""

from pydantic_settings import BaseSettings


class FastAPI(BaseSettings):
    """Configuração de FastAPI."""

    root_path: str = "/tria-api"

    class Config:
        """Model configuration."""

        env_prefix = "fastapi_"


fastapi = FastAPI()
