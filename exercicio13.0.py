idade = int(input('Digite sua idade: '))

if idade < 16:
    print(f'Idade: {idade} - Não eleitor.')
elif idade >= 18 and idade <= 65:
    print(f'Idade: {idade} - Eleitor obrigatorio.')
else:
    print(f'Idade: {idade} - Eleior facutativo.')