"""
6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
“Nota válida”, senão “Nota inválida”.
Entrada: 3.5 Saída: Nota válida
Entrada: 11.5 Saída: Nota Inválida
"""

nota = float(input(f"Digite uma nota: "))
if nota <= 10:
    print(f"Nota válida!")
else:
    print(f"Nota inválida!")
