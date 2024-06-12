sexo = input('Digite seu sexo: ')
altura = float(input('Digite sua altura: '))

pesoideal = 0.0 
if sexo.upper() == 'M':
    pesoideal = (72.7*altura)-58
elif sexo.upper == 'F' :
    pesoideal = (62.1*altura)-44.7
else:
    print('O sexo informado deve ser 'M' para masculino ou 'F' para feminino')

if(pesoideal >0):
    print('Sexo informado foi: ', sexo.upper())
    print('Peso ideal: ', round(pesoideal, 2))