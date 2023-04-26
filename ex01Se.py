"""
1. Dado um número pelo usuário, verificar se ele é positivo, exibindo a mensagem “O numero é
positivo” ou “O numero não é positivo”.
Entrada: 45 Saída: O numero é positivo
Entrada: -3 Saída: O numero não é positivo
Entrada: 0 Saída: O numero não é positivo

"""
num = float(input("Digite um numero: "))
if num > 0:
    print("O número é positivo")
else:
    if num < 0:
        print("O número não é positivo")
    if num == 0:
        print("O número não é positivo")