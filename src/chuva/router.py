"""Roteamento das rotas relativas à chuva."""

from fastapi import APIRouter

from src.chuva.rotas import diaria

rotas_chuva = APIRouter(prefix="/chuva")
rotas_chuva.include_router(diaria.router)
