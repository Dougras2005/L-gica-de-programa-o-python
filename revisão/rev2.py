preco = float(input('Digite o preço: '))
print('1 - Á vista no dinheiro ou cheque.')
print('2 - Á vista no cartão de crédito.')
print('3 - Em Duas vezes no cartão de crédito.')
print('4 - Em Três vezes no cartão de crédito, com 10% de juros')
pagamento = int(input('Forma de pagamento: '))

if pagamento == 1:
    valor = preco - 10/100 * preco
    print(f'O valor do pagamento sera de: {valor}.')
elif pagamento == 2:
    valor = preco - 15/100 * preco
    print(f'o Valor do pagamento sera de: {valor}')
elif pagamento == 3:
    valor = preco /2 
    print(f'O valor das parcelas em 2x sera de: {valor}.')
elif pagamento == 4:
   valor = preco + 10/100 * preco
   print(f'O valor total sera {valor}.')
   valor = valor /3
   print(f'O valor das parcelas em 3x sera de: {valor}.')

else:
    print('Forma de pagamento inválida.')