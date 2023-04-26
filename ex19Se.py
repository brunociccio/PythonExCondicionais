"""
19. Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Se formar, exibir a mensagem “Forma um triângulo”, senão “Não forma um triângulo”.
Entrada: 10 11 12 Saída: Forma um triângulo
Entrada: 2 7 10 Saída: Não forma um triângulo
Entrada: 4 7 7 Saída: Forma um triângulo
Entrada: 34 10 14 Saída: Não forma um triângulo
Entrada: 15 15 15 Saída: Forma um triângulo

"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num = num1 + num2
if num2 >= num1 and num >= num3:
    print("forma um triangulo")
else:
    print("não forma um triangulo")
