"""
15. Dados três números pelo usuário, analisá-los e exibir a mensagem “3 números diferentes”, “2 dos 3
são iguais” ou “3 números iguais”.
Entrada: 1 2 3 Saída: 3 números diferentes
Entrada: 1 2 2 Saída: 2 dos 3 são iguais
Entrada: 2 1 2 Saída: 2 dos 3 são iguais
Entrada: 2 2 1 Saída: 2 dos 3 são iguais
Entrada: 3 3 3 Saída: 3 números iguais
"""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
if n1 == n2 and n1 == n3:
    if n2 == n3:
        print(f"Os três números são iguais!")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print(f"Dois dos três números são iguais!")
else:
    print("os três números são diferentes!")

