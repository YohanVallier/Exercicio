import requests

def consultar_cep(cep_texto):

	cep_limpo=cep_texto.replace("-", "").replace(".", "").strip()
	
	if len(cep_limpo) != 8 or not cep_limpo.isdigit():
		return None

	url=f"https://viacep.com.br/ws/{cep_limpo}/json/"

	try:
		resposta=requests.get(url, timeout=5)
		resposta.raise_for_status()
		
		if resposta.status_code==200:
			dados=resposta.json()
			rua=dados.get("logradouro")
			bairro=dados.get("bairro")
			cidade=dados.get("localidade")
			if "erro" not in dados:
				return print(f"{dados}\n\nEndereço encontrado: {rua}, {bairro} - {cidade}")
	except requests.exceptions.RequestException as erro:
		return None
