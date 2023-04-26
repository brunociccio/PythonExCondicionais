"""
3. Dado um número pelo usuário, verificar se ele é “O número é par” ou “O número é impar”,
exibindo sua respectiva mensagem.
Entrada: 3 Saída: O numero é impar
Entrada: 10 Saída: O numero é par
"""

num = float(input(f"Digite um número: "))
result =  num % 2
if result == 0:
    print(f"O número é par!")
else:
    print(f"O número é impar!")