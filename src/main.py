"""Módulo principal da API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src.config import fastapi

app = FastAPI(
    root_path=fastapi.root_path,
    docs_url="/docs",
    openapi_url="/openapi.json",
    title="Desafio TRIA API",
    description="API for Trio challenge",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def root() -> str:
    """
    Endpoint para checagem de estado da API.

    Returns
    -------
    str
        Menssagem indicando que está funcionando.
    """
    return "Bem-vindo a API de desafio da TRIA!"


# encapsulation with mangum for API Gateway compatibilization.
handler = Mangum(app=app, api_gateway_base_path=fastapi.root_path)
