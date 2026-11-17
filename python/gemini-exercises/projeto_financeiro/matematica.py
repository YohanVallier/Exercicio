def calcular_juros_compostos(capital: float, taxa_decimal: float, periodo_meses: float):
    M = capital*((1+taxa_decimal)**periodo_meses)
    return M
