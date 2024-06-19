sexo = input('Digite o sexo: ')
altura = float(input('Digite sua altura: '))

if sexo.upper() == 'M':
    pesoideal = (72.7*altura)-58
elif sexo.upper() == 'F':
    pesoideal = (62.1*altura)-44
else:
    print('Erro!! Digite o sexo correto, M para masculino e F para feminino.') 

if(pesoideal >0):
    print('Sexo informado foi: ', sexo.upper())
    print('Peso ideal: ', round(pesoideal, 2))
