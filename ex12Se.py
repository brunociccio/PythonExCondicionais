"""
12. Dada a tabela de cálculo do IR:
Salário-de-contribuição (R$) Alíquota Dedução (R$)
até 1.710,78 isento 0
de 1.710,79 até 2.563,91 7,5% 128,31
de 2.563,92 até 3.418,59 15% 320,60
de 3.418,60 até 4.271,59 22,5% 577,00
Acima de 4.271,59 27,5% 790,58
Fazer um algoritmo que leia o salário do contribuinte e calcule quanto ele terá que pagar de
Imposto de Renda (IR).
Entrada: 1100.00 Saída: 0.00
Entrada: 2000.00 Saída: 21.69
Entrada: 3123.45 Saída: 147.91
Entrada: 3891.12 Saída: 298.50
Entrada: 9000.00 Saída: 1684.42
"""
sal = float(input("Digite seu salário: "))
if sal <= 1710.78:
    ir = 0
elif sal >= 1710.79 and sal <= 2563.91:
    ir = (sal * 0.075) - 128.31
elif sal >= 2563.92 and sal <= 3418.59:
    ir = (sal * 0.15) - 320.60
elif sal >= 3418.60 and sal <= 4271.59:
    ir = (sal * 0.225) - 577.00
elif sal > 4271.59:
    ir = (sal * 0.275) - 790.58

sal_liq = sal - ir
print(f"""
    Salário..........: {sal: 4.2f}
    IR...............: {ir: 4.2f}
    Salário Líquido..: {sal_liq: 4.2f}

    Obrigado por usar nosso sistema!
""")