"""
18. Dados 3 numero pelo usuário, verificar se são diferentes, se forem exibir o numero com valor
intermediário, senão (se houver 2 ou 3 números iguais) exibir a mensagem “Os números não são
diferentes”.
Entrada: 4 9 7 Saída: 7
Entrada: 14 7 7 Saída: Os números não são diferentes
Entrada: 12 2 30 Saída: 12
Entrada: 3 3 3 Saída: Os números não são diferentes
Entrada: 45 67 76 Saída: 67
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
        print("O número intermediário é:", num1)
    elif num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
        print("O número intermediário é:", num2)
    else:
        print("O número intermediário é:", num3)
else:
    print("Os números não são diferentes.")
