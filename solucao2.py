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
