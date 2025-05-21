"""Configurações de chuva."""

from pathlib import Path

import pandas as pd
from pydantic_settings import BaseSettings


class ConfiguracoesChuva(BaseSettings):
    """Configuracoes do back de chuva."""

    caminho_csvs: Path = Path("arquivos")

    @property
    def obter_dataframe_chuva(self) -> pd.DataFrame:
        """
        Junta os dados em um só dataframe.

        Returns
        -------
        pd.DataFrame
            Dataframe concatenados;
        """
        arquivos_csv = list(self.caminho_csvs.glob("*.csv"))
        df = pd.concat(
            (pd.read_csv(arquivo) for arquivo in arquivos_csv), ignore_index=True
        )
        df = df.drop(columns="Unnamed: 0")
        return df


config = ConfiguracoesChuva()
