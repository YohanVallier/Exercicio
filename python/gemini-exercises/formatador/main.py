import requests # Biblioteca externa instalada via pip
from formatador import formatar_moeda # Módulo próprio criado na mesma pasta

try:
    # Consultando a API pública de cotações AwesomeAPI
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url)
    
    # Converte o JSON retornado em um dicionário Python
    dados = resposta.json()
    cotacao_usd = float(dados["USDBRL"]["bid"])
    
    print(f"Cotação atual do Dólar: {formatar_moeda(cotacao_usd)}")

except Exception as erro:
    print(f"Falha ao consultar cotação: {erro}")
