import pandas as pd
import requests
def carregar_csv(caminho: str) -> pd.DataFrame:
    """Carrega um ficheiro CSV e retorna um DataFrame."""
    df = pd.read_csv(caminho, encoding='utf-8')
    print(f"✅ Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas")
    return df
def guardar_csv(df: pd.DataFrame, caminho: str) -> None:
    """Guarda o DataFrame num ficheiro CSV/Excel.
    df.to_csv(caminho, index=False)"""
    df.to_excel(caminho, index=False,engine='openpyxl')
    print(f"✅ Ficheiro guardado: {caminho}")
    
