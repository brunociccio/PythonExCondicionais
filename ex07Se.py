"""
7. Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, caso uma (ou as duas)
nota seja inválida exibir “Nota inválida!” e terminar o algoritmo; senão, calcular e exibir a média e
exibir se está aprovado (vide saída do exercício anterior).
Entrada: 10.0 4.0 Saída: 7.0 – Você está aprovado
Entrada: 2.0 3.0 Saída: 2.5 – Você está reprovado
Entrada: 14.0 Saída: Nota Inválida!
Entrada: 5.0 -6.0 Saída: Nota Inválida!
"""

nota1 = float(input("Digite a primeira nota: "))
if nota1 >=0 and nota1 <=10:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 >=0 and nota2 <=10:
        med = (nota1 + nota2) / 2
        if med >= 6:
            print(f"Sua média é '{med}'.Você está aprovado!")
        else:
            print(f"Sua mé dia é '{med}'.Você está reprovado!")
    else:
        print("Nota 2 inválida!")
else:
    print("Nota 1 inválida!")




