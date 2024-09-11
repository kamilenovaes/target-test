'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

string = "Teste técnico para o estágio na empresa Target"

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1): # percorre a string de trás para frente
        invertida = invertida + s[i]
    return invertida

invertida = inverter_string(string)
print(f"Original: {string}")
print(f"Invertida: {invertida}")

# Resposta:
# Original: Teste técnico para o estágio na empresa Target
# Invertida: tegraT aserpme an oigátse o arap ocincét etseT