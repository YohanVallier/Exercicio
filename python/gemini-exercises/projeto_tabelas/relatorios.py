from tabulate import tabulate

def gerar_tabela_vendas(dados, cabecalho):
    return print(tabulate(dados, headers=cabecalho, tablefmt="grid"))
