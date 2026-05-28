import pandas as pd

def resumo_dados(df: pd.DataFrame) -> None:
    """Exibe um resumo geral do DataFrame."""
    print("=== RESUMO DOS DADOS ===")
    print(f"Dimensões: {df.shape}")
    print(f"\nTipos de dados:\n{df.dtypes}")
   

def converter_tipos(df: pd.DataFrame, conversoes: dict = None) -> pd.DataFrame:
    """Converte colunas com base num dicionário {coluna: tipo}."""
    
    if conversoes:
        for col, tipo in conversoes.items():
            if tipo == 'data':
                df[col] = pd.to_datetime(df[col],dayfirst=True)
            elif tipo == 'moeda':
                df[col] = (
                    df[col]
                    .str.replace(',', '')
                    .str.replace('$', '')
                    .astype(float)
                )
    
    return df