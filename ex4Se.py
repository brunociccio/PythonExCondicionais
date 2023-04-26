"""
4. Dados dois números pelo usuário, exibir o de maior valor.
Entrada: 5 45 Saída: 45
Entrada: 10 8 Saída: 10
"""

num1 = float(input(f"Digite um número: "))
num2 = float(input(f"Digite outro número: "))
if num1 < num2:
     print(f"O maior número digitado pelo usuário é: {num2}")
else:
    print(f"O maior número digitado pelo usuário é: {num1}")


