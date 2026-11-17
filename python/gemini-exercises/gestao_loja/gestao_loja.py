metodos_pagamento = ("PIX", "Boleto", "Cartão")

produto_atual = {"nome": "Teclado", "preco": 150.00, "quantidade": 2}

produto_atual["total"] = produto_atual["preco"] * produto_atual["quantidade"]

carrinho_de_compras = []

carrinho_de_compras.append(produto_atual)

print(metodos_pagamento)
print(carrinho_de_compras)
