"""
10. Dentre três números dados pelo usuário, verificar e exibir o de maior valor.
Entrada: 10 6 17 Saída: 17
Entrada: 5 15 10 Saída: 15
Entrada: 5 -1 0 Saída: 5
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O maior número é: {num3}")