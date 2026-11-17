from validadores import validar_positivo as vap
from matematica import calcular_juros_compostos as juros_comp

capital = float(input("Qual o valor do capital? "))
taxa = float(input("Qual o valor da taxa? "))
periodo = float(input("Qual o período em meses? "))

c = vap(capital)
t = vap(taxa)
p = vap(periodo)

try:
    if c and t and p:
        resultado = juros_comp(c, t, p)
        print(f"\nMontante final calculado: R$ {resultado:.2f}")
    else:
        print("\nErro de validação: Todos os valores digitados devem ser maiores que zero.")

except ValueError:
    print("\nErro de entrada: Digite apenas números inteiros ou decimais válidos.")
