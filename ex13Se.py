"""
13. Juntar os dois exercícios anteriores, ou seja, pedir a digitação do Salário Bruto e calcular o INSS e IR
devido. Exibir o Salário Bruto, INSS, IR e Salário Líquido.
Entrada: 1043.12 Saída: 1043.12 84.45 0.00 959.67
Entrada: 1795.42 Saída: 1795.42 161.59 134.66 1499.18
Entrada: 3011.45 Saída: 3011.45 331.26 451.72 2228.47
Entrada: 3891.12 Saída: 3891.12 428.02 875.50 2587.59
Entrada: 9000.00 Saída: 9000.00 468.00 2475.00 6057.00
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

sal_liq = sal - (inss + ir)

print(f"""
    Salário Bruto....: {sal: 4.2f}
    INSS.............: {inss: 4.2f}
    IR...............: {ir: 4.2f}
    Salário Líquido..: {sal_liq: 4.2f}
    
    Obrigado por usar nosso sistema!
    """)