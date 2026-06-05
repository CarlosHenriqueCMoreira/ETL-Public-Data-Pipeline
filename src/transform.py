import pandas as pd

def transformar(dados):
    # cria um DataFrame a partir da lista de dicionários
    df = pd.DataFrame(dados)
    
    # renomeia as colunas para português
    df = df.rename(columns={
        "cotacaoCompra": "compra",
        "cotacaoVenda": "venda",
        "dataHoraCotacao": "data_hora"
    })
    
    # converte a coluna data_hora para formato datetime
    df["data_hora"] = pd.to_datetime(df["data_hora"])
    
    # remove linhas com valores nulos
    df = df.dropna()
    
    # ordena por data
    df = df.sort_values("data_hora")
    
    # reseta o índice após ordenação
    df = df.reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    # dados de teste simulando o retorno da API
    dados_teste = [
        {"cotacaoCompra": 4.97, "cotacaoVenda": 4.971, "dataHoraCotacao": "2024-01-02 10:08:29"},
        {"cotacaoCompra": 4.95, "cotacaoVenda": 4.951, "dataHoraCotacao": "2024-01-02 11:08:29"},
    ]
    df = transformar(dados_teste)
    print(df)
    print(df.dtypes)