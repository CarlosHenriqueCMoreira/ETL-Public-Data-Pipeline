import requests
import pandas as pd
from datetime import datetime
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"

def validar_datas(data_inicio, data_fim):
    try:
        inicio = datetime.strptime(data_inicio, "%m-%d-%Y")
        fim = datetime.strptime(data_fim, "%m-%d-%Y")
        if inicio > fim:
            raise ValueError("Data de início maior que data fim")
        return True
    except ValueError as e:
        logging.error(f"Erro na validação de datas: {e}")
        return False

def montar_url(data_inicio, data_fim):
    endpoint = "CotacaoDolarPeriodo"
    url = (
        f"{BASE_URL}/{endpoint}"
        f"(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        f"?@dataInicial='{data_inicio}'"
        f"&@dataFinalCotacao='{data_fim}'"
        f"&$format=json"
    )
    return url

def fazer_requisicao(url, tentativas=3):
    for i in range(tentativas):
        try:
            logging.info(f"Tentativa {i+1} de {tentativas}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            logging.warning("Timeout, tentando novamente...")
            time.sleep(2)
        except requests.exceptions.HTTPError as e:
            logging.error(f"Erro HTTP: {e}")
            break
    return None

def extrair_cotacao_dolar(data_inicio, data_fim):
    logging.info(f"Iniciando extração: {data_inicio} até {data_fim}")

    if not validar_datas(data_inicio, data_fim):
        return None

    url = montar_url(data_inicio, data_fim)
    logging.info(f"URL montada: {url}")

    response = fazer_requisicao(url)

    if response is None:
        logging.error("Falha na requisição")
        return None

    dados = response.json()["value"]
    logging.info(f"{len(dados)} registros extraídos")
    return dados

if __name__ == "__main__":
    resultado = extrair_cotacao_dolar("01-01-2024", "01-31-2024")
    if resultado:
        print(resultado[:3])