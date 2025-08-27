import typer
import requests
import logging

from .config.logging_config import setup_logging
from .config.settings import settings

app = typer.Typer(add_completion=False, pretty_exceptions_enable=False)
setup_logging()

logger = logging.getLogger(__name__)

logger.info(f"🚀 Aplicação iniciando no ambiente: {settings.env.upper()}")


def cotacao_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data["USDBRL"]["bid"])
    except requests.RequestException as e:
        logger.error("Erro na requisição:", e)
        return None
    except (KeyError, ValueError):
        logger.error("Erro ao processar os dados da API")
        return None
    

@app.command()
def run():
    valor = cotacao_dolar()
    if valor is not None:
        logger.info(f"Cotação atual do dólar: R$ {valor:.4f}")

if __name__ == "__main__":
    app()




    