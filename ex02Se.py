"""
2. Dada uma idade pelo usuário, verificar e exibir a mensagem “Você é menor de Idade” ou “Você é
maior de Idade”.
Entrada: 15 Saída: Você é menor de Idade
Entrada: 33 Saída: Você é maior de Idade

"""

idade = float(input(f"Digite a sua idade: "))
if idade < 18:
    print(f"Você é menor de idade")
else:
    if idade > 18:
        print(f"Você é maior de idade")
    if idade == 18:
        print(f"Você é maior de idade")