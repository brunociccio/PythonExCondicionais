"""
8. Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).
Entrada: 3 Saída: Positivo
Entrada: -5 Saída: Negativo
Entrada: 0 Saída: Nulo

"""

num = float(input("Digite um número: "))
if num >0:
    print(f"Positivo!")
elif num <0:
    print(f"Negativo!")
elif num ==0:
    print(f"Nulo!")

