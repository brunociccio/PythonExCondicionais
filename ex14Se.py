"""
14. Dados três números pelo usuário, exibi-los em ordem crescente.
Entrada: 1 2 3 Saída: 1 2 3
Entrada: 1 3 2 Saída: 1 2 3
Entrada: 2 1 3 Saída: 1 2 3
Entrada: 2 3 1 Saída: 1 2 3
Entrada: 3 1 2 Saída: 1 2 3
Entrada: 3 2 1 Saída: 1 2 3
"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"A ordem crescente dos números é: {n3}, {n2} e {n1}")
    else:
        print(f"A ordem crescente dos números é: {n2}, {n3} e {n1}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"A ordem crescente dos números é: {n3}, {n1} e {n2}")
    else:
        print(f"A ordem crescente dos números é: {n1}, {n3} e {n2}")
else:
    if n1 > n2:
        print(f"A ordem crescente dos números é: {n2}, {n1} e {n3}")
    else:
        print(f"A ordem crescente dos números é: {n1}, {n3} e {n2}")