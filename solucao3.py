'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

## Observação: O teste não fornece o arquivo JSON ou XML, então criei um arquivo JSON hipotético para testar.

import json

with open('faturamento.json', 'r') as f:
    dados_faturamento = json.load(f)

faturamento_diario = dados_faturamento['faturamento_diario']
faturamento_valido = [valor for valor in faturamento_diario if valor > 0] # fins de semana ou feriados = 0

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_faturamento])

print(f"O menor valor de faturamento ocorrido em um dia do mês: R$ {menor_faturamento:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: R$ {maior_faturamento:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_da_media}")
