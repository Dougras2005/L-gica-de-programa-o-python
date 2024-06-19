ano_nacimento = int(input('Digíte o ano: '))
ano_atual = int(input('Digíte o ano atual: '))

if ano_nacimento > 0:
    idade = ano_nacimento - ano_atual
    print(f'De acordo com os anos informado a idade é {idade}.')