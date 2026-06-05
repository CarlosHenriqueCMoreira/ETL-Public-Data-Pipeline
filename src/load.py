from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

# carrega as variáveis do arquivo .env
load_dotenv(dotenv_path="../.env")

def criar_conexao():
    # monta a string de conexão com as variáveis do .env
    string_conexao = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    # cria e retorna o engine de conexão com o banco
    engine = create_engine(string_conexao)
    return engine

def carregar(df):
    # cria a conexão com o banco
    engine = criar_conexao()
    
    # salva o DataFrame na tabela "cotacao_dolar"
    # if_exists="replace" apaga e recria a tabela a cada execução
    # index=False não salva o índice do pandas como coluna
    df.to_sql("cotacao_dolar", engine, if_exists="replace", index=False)
    
    logging.info(f"{len(df)} registros carregados no banco com sucesso!")

if __name__ == "__main__":
    import pandas as pd
    
    # dados de teste para validar a carga
    dados_teste = pd.DataFrame([
        {"compra": 4.97, "venda": 4.971, "data_hora": "2024-01-02 10:08:29"},
        {"compra": 4.95, "venda": 4.951, "data_hora": "2024-01-02 11:08:29"},
    ])
    
    carregar(dados_teste)
    print("Dados carregados com sucesso!")