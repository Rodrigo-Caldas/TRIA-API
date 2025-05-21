from typing import Literal

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.chuva.logica import diaria

router = APIRouter()


@router.get("/datas-disponiveis")
def buscar_datas_disponiveis(
    codigo: Literal["1547079", "2244107", "3051043", "9999999"],
) -> JSONResponse:
    """
    Busca as datas disponíveis a partir de um código de estação.

    Parameters
    ----------
    codigo : Literal["1547079", "2244107", "3051043", "9999999"]
        Códigos aceitos.

    Returns
    -------
    JSONResponse:
        Datas disponíveis para o código escolhido.
    """
    datas = diaria.buscar_datas_disponiveis(codigo)
    return JSONResponse(content=jsonable_encoder(datas))
