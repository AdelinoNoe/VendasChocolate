from src.Carregar_Df import carregar_csv,guardar_csv
from src.limpeza import resumo_dados,converter_tipos

def main():
    # 1. Carregar dados
    df = carregar_csv("data/raw/Chocolate Sales.csv")

    # 2. Explorar dados
    resumo_dados(df)
    # 3. Limpar dados
    df = converter_tipos(
        df, conversoes=
        {
            'Date': 'data',
            'Amount': 'moeda'
             }
            )
    print("Depois:", df['Date'].dtype)
    print("Depois:", df['Amount'].dtype)
    print(df['Date'].head())
    print("\n✅ Análise concluída! Resultados em /outputs/graficos")
    guardar_csv(df, "data/processed/Chocolate_Sales_final.csv") 

if __name__ == "__main__":
    main()