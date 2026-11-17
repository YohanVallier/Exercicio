def formatar_moeda(valor):
    # Recebe um float e retorna uma string formatada em Reais
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
