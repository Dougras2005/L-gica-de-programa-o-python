a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = b*b - 4*a*c #b**2

if delta < 0:
    print(f'{delta} Não há raiz.')
if delta == 0:
    print(f'Delta: {delta} - Não é equação de segundo grau.')
else:
    raiz1 = (-b + (delta**0.5)) /2*a

    raiz2 = (-b - (delta**0.5)) / 2*a

    print(f'Delta: {delta} - raiz 1: {raiz1}, raiz2: {raiz2}')