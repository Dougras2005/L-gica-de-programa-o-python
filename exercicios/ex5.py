try:
    sexo = input('Digite seu sexo: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('digite seu peso: '))
except Exception as e:
    print('Houve algum erro', e)
else:

    pesoideal = 0.0 
    if sexo.upper() == 'M':
        pesoideal = (72.7*altura)-58
    elif sexo.upper == 'F' :
        pesoideal = (62.1*altura)-44.7
    else:
        print('O sexo informado deve ser M para masculino ou F para feminino')

    if(pesoideal >0):
        print('Sexo informado foi: ', sexo.upper())
        print('Peso ideal: ', round(pesoideal, 2))

    imc = float(pesoideal/(altura**2))
    print('Seu IMC é', imc)

    if imc <18.5:
        print('Abaixo do peso.')
    elif imc >= 18.5 < 25:
        print('Peso normal.')
    elif imc >= 25 < 30:
        print('Sobrepeso.')
    elif imc >= 30 < 35:
        print('Obesidade grau 1.')
    elif imc >= 35 < 40:
        print('Obesidade grau 2.')
    else:
        print('Obesidade grau 3.')
    
finally:
    print('fim do progrma!')