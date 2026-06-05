import logging
import sys
sys.path.append(".")

# importa as funções dos outros módulos
from extract import extrair_cotacao_dolar
from transform import transformar
from load import carregar

# configura o log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def executar_pipeline(data_inicio, data_fim):
    logging.info("=== INICIANDO PIPELINE ETL ===")
    
    # EXTRACT — busca os dados da API
    logging.info("Etapa 1: Extraindo dados da API...")
    dados = extrair_cotacao_dolar(data_inicio, data_fim)
    
    # para o pipeline se não vieram dados
    if not dados:
        logging.error("Nenhum dado extraído. Encerrando pipeline.")
        return
    
    # TRANSFORM — limpa e transforma os dados
    logging.info("Etapa 2: Transformando dados...")
    df = transformar(dados)
    
    # LOAD — salva no banco de dados
    logging.info("Etapa 3: Carregando dados no banco...")
    carregar(df)
    
    logging.info("=== PIPELINE CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    # define o período de extração
    executar_pipeline("01-01-2024", "12-31-2024")
    