from relatorios import gerar_tabela_vendas as gtv

lista_produtos = [["Geladeira Brastemp Frost Free 385L", "20", "2.698,54"], 
                  ["Smartphone Motorola Moto g05 256GB", "50", "899"],
                  ["Smart TV 43 Philco Roku TV HDR10 Dolby Audio P43CRA", "120", "2.067,06"]]

cabecalho = ["Nome", "Quantidade", "Preço Unitário"]

gtv(lista_produtos, cabecalho)
