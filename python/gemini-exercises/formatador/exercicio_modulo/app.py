from calculos import calcular_imposto as calc

lista_faturamento=[1000.0, 2500.0, 5000.0]
for lista in lista_faturamento:
    print(calc(lista, 0.15))
