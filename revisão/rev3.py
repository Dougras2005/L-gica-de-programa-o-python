total = 0
while True:

    produto = input('Digíte o produto: ')
    quant = int(input('Digíte a quantidade: '))
    preco = float(input('Preço: '))
    total = total + quant * preco

    s = input('Digite s para sair ou enter para continuar ')
    if s.upper():
        break
print(f'Total da compra: {total}')