import re

relatorio_bruto = """
[2026-11-10] Faturamento confirmado - NF-2026-0041 - Valor: R$ 1.250,00
[2026-11-11] Falha na emissão - Erro interno do servidor
[2026-11-12] Faturamento confirmado - NF-2026-0042 - Valor: R$ 890,50
[2026-11-14] Cancelamento - NF-2025-9981 - Estorno realizado
[2026-11-15] Faturamento confirmado - NF-2026-0105 - Valor: R$ 3.400,00
"""

padrao_notas = r"\bNF-2026-\d{4}\b"
padrao_moeda = r"R\$\s+[\d.]+,\d{2}\b"

notas_2026 = re.findall(relatorio_bruto, padrao_notas)
valores_brutos = re.findall(relatorio_bruto, padrao_moeda)

valores_float = [
    float(re.sub(r"R\$\s*|\.", "", valores).replace(",", "."))
    for valores in valores_brutos
]