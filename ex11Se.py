"""
11. Dada a tabela de cálculo do INSS:
Salário Alíquota para fins de recolhimento
ao INSS (%)
até 1.247,70 8,00
de 1.247,71 até 2.079,50 9,00
de 2.079,51 até 4.159,00 11,00
Acima de 4.159,00 Cobrar teto de 468,00
Fazer um algoritmo que leia o salário do contribuinte e calcule quanto ele irá pagar de INSS.
Entrada: 1100.00 Saída: 88.00
Entrada: 2000.00 Saída: 180.00
Entrada: 3456.78 Saída: 380.24
Entrada: 9000.00 Saída: 468.00
"""
sal = float(input("Digite seu salário: "))
if sal <= 1247.70:
    inss = (sal * 0.08)
elif sal >= 1247.71 and sal <= 2079.50:
    inss = (sal * 0.09)
elif sal >= 2079.51 and sal <= 4159.00:
    inss = (sal * 0.11)
elif sal > 4159.00:
    inss = 468.00
sal_liq = sal - inss
print(f"""
    Salário..........: {sal: 4.2f}
    INSS.............: {inss: 4.2f}
    Salário Líquido..: {sal_liq: 4.2f}

    Obrigado por usar nosso sistema!
""")
