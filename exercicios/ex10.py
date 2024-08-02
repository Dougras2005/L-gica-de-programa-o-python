def mensagem(a):
    print(f'Seja bem vindo(a) {a}!!!')

def dobro(x):
    return 2*x

nome = input('Digite seu nome: ')
mensagem(nome)

numero = int(input('Digite o nuúmero: '))
print(f'O dobro de {numero} é {dobro(numero)}')