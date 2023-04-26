"""
16. Dado o salário de uma pessoa, sexo (1 para Masculino e 2 para Feminino) e idade, verificar a tabela
abaixo e calcular a devida cobrança de convênio médico sobre o salário informado:
Idade Masculino Feminino
Até 20 anos 5,34% 3,56%
Acima de 20 até 40 anos 8,44% 6,43%
Acima dos 40 anos 10,12% 8,02%
Entrada: 1500.00 1 45 Saída: Valor do convenio: R$ 80.10
Entrada: 1600.00 2 42 Saída: Valor do convenio: R$ 56.96
Entrada: 2123.43 1 19 Saída: Valor do convenio: R$ 113.39
Entrada: 2600.00 2 18 Saída: Valor do convenio: R$ 92.96
Entrada: 2000.00 1 30 Saída: Valor do convenio: R$ 168.80
Entrada: 2000.00 2 29 Saída: Valor do convenio: R$ 128.60
"""
sal = float(input(f"Digite o seu salário: "))
sexo = float(input(f"Digite [1]Masculino ou [2]Feminino: "))
idade = float(input(f"Digite a sua idade: "))
if idade <= 20 and sexo == 1:
    conv = sal * 0.0534
elif idade <= 20 and sexo == 2:
    conv = sal * 0.0356
elif idade <= 40 and sexo == 1:
    conv = sal * 0.0844
elif idade <= 40 and sexo == 2:
    conv = sal * 0.0643
elif idade >= 41 and sexo == 1:
    conv = sal * 0.1012
elif idade >= 41 and sexo == 2:
    conv = sal * 0.0802
print(f"O valor do seu convênio é de R$ {conv}")