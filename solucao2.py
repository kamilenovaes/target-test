'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''


def fibonacci(n):
    a = 0
    b = 1
    
    # Caso base
    if n == 0: 
        return True
    
    # Calcula a sequência de Fibonacci até o número
    while b <= n:
        if b == n:
            return True
        temp = b
        b = a + b
        a = temp
    
    return False

# Número escolhido
num = 34

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

# Resposta (para este número): O número 34 pertence à sequência de Fibonacci.
