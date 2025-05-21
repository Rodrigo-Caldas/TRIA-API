"""Módulo de lógica de chuva diária."""

from typing import Literal

import pandas as pd

from src.chuva.config import config
from src.chuva.modelos import DatasDisponiveis


def buscar_datas_disponiveis(
    codigo: Literal["1547079", "2244107", "3051043", "9999999"],
) -> DatasDisponiveis:
    """
    Busca as datas disponíveis a partir de um código de estação.

    Parameters
    ----------
    codigo : Literal[1547079, 2244107, 3051043, 9999999]
        Códigos aceitos.

    Returns
    -------
    DatasDisponiveis
        Datas disponíveis para o código escolhido.
    """
    codigo_int = int(codigo)
    df = config.obter_dataframe_chuva

    df_filtrado = df.loc[df["codigo"] == codigo_int].copy()
    df_filtrado["datas"] = pd.to_datetime(df_filtrado["data"])
    df_filtrado = df_filtrado.drop(columns=["chuva", "codigo", "data"])

    datas = {"datas": list(df_filtrado["datas"])}

    objeto = DatasDisponiveis(**datas)

    return objeto
