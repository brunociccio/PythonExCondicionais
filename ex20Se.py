"""
20. Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Em caso afirmativo, informar ao usuário se o triângulo é equilátero (três lados iguais),
isósceles (dois lados iguais) ou escaleno (três lados diferentes). Em caso negativo, exibir “Não forma
um triângulo”.
Entrada: 10 11 12 Saída: Triângulo Escaleno
Entrada: 2 7 10 Saída: Não forma um triângulo
Entrada: 4 7 7 Saída: Triângulo Isósceles
Entrada: 34 10 14 Saída: Não forma um triângulo
Entrada: 15 15 15 Saída: Triângulo Equilátero
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    if num1 == num2 and num2 == num3:
        print("O triangulo é equilatero!")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print("O trinagulo é isósceles!")
    else:
        print("O triangulo é escaleno!")
else:
    print("Não forma triangulo")
