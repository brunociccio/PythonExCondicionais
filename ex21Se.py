"""
21. Dado o ano pelo usuário, verificar se o ano é bissexto exibindo a mensagem “Ano bissexto” ou
“Não é ano bissexto”. Sabe-se que o ano bissexto é aquele que é múltiplo de 4, exceto os múltiplos
de 100 que não sejam múltiplos de 400. Por exemplo: 1996, 2004, 2008, 2012, 1600, 2000 e 2400
(são bissextos); 1700, 1800, 1900 e 2100 (não são bissextos).
Entrada: 2013 Saída: Não é ano bissexto
Entrada: 2008 Saída: É ano bissexto
Entrada: 1881 Saída: Não é ano bissexto
Entrada: 2012 Saída: É ano bissexto
"""
ano = float(input("Digite o ano: "))
if ano % 4 == 0:
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")


