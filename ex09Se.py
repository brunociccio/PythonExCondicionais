"""
Dadas três notas (AV1, AV2 e AV3), fazer um algoritmo que calcule a media. A média consiste em
descartar a menor nota entre as 3 médias calculando a média simples das outras duas. Exibir se o
aluno está “Aprovado” ou “Reprovado” (média menor do que 6).
Entrada: 3.0 7.0 5.0 Saída: 5.0 - Reprovado
Entrada: 5.5 6.0 7.5 Saída: 6.5 – Aprovado
"""
av1 = float(input("Digite a sua primeira nota: "))
av2 = float(input("Digite a sua segunda nota: "))
av3 = float(input("Digite a sua terceira nota: "))
if av1 > av2 and av2 < av3:
    med = (av1 + av3)/2
if av1 > av3 and av2 > av3:
    med = (av1 + av2)/2
if av1 < av2 and av1 < av3:
    med = (av2 + av3)/2
    if med >= 6:
        print(f"Sua média é: {med}. Você está Aprovado!")
else:
    print(f"Sua média é {med}. Você está Reprovado!")
