"""
5. Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5
exibir “Você está reprovado”, senão exibir “Você está aprovado”.
Entrada: 7.0 5.0 Saída: 6.0 – Você está aprovado
Entrada: 4.5 3.5 Saída: 4.0 – Você está reprovado
"""

nota1 = float(input(f"Digite a nota 1: "))
nota2 = float(input(f"Digite a nota 2: "))
med = (nota1 + nota2)/2
print(f"Sua média é: {med}")
if med >= 6:
    print(f"Você está aprovado!")
else:
    med < 6
    print(f"Você está reprovado!")