"""
17. Um professor usa Provas e Atividades para compor a nota AV1. Ele usa 2 provas e 4 atividades (os
valores são digitados nesta ordem). A média das provas vale 60% da AV1 enquanto que as
atividades valem 0 ou 1 ponto cada. Considerando que a media é 6,0 faça um algoritmo que calcule
a AV1 e mostre a mensagem: “AV1 = X.X, você está acima da média.”, “AV1 = 6.0, você está na
média.” ou “AV1 = X.X, você está abaixo da média.”.
Entrada: 4.0 5.0 1 1 1 0 Saída: AV1 = 5.7, você está abaixo da média.
Entrada: 6.0 4.0 0 1 1 1 Saída: AV1 = 6.0, você está na média.
Entrada: 7.0 5.0 1 1 1 1 Saída: AV1 = 7.6, você está acima da média.
"""
prova1 = float(input(f"Digite a nota da prova 1: "))
prova2 = float(input(f"Digite a nota da prova 2: "))
ava1 = float(input(f"Digite a nota da avaliação 1: "))
ava2 = float(input(f"Digite a nota da avaliação 2: "))
ava3 = float(input(f"Digite a nota da avaliação 3: "))
ava4 = float(input(f"Digite a nota da avaliação 4: "))
prova = ((prova1 + prova2)/2) * 0.6
av1 = prova + ava1 + ava2 + ava3 + ava4
if av1 < 6:
    print(f"Sua nota é '{av1:.2f}'. Você está abaixo da média")
elif av1 == 6:
    print(f"Sua nota é '{av1:.2f}'. Você está na média")
else:
    print(f"Sua nota é '{av1:.2f}'. Você está acima da média")



