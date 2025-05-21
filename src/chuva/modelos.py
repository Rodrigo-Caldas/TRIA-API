"""Esquemas de chuva."""

from datetime import datetime
from typing import List

from pydantic import BaseModel


class DatasDisponiveis(BaseModel):
    """
    Datas disponíveis de chuva.

    Attributes
    ----------
    datas : List[datetime]
        Lista de datas disponíveis.
    """

    datas: List[datetime]
