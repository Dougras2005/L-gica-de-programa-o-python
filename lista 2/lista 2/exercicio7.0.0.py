somaIdade = 0
cont = 0 

while True:
    try:
        idade = int(input('Digie a idade (para encerrar digite zero): '))
        if  idade > 0:
            somaIdade =+ idade
        elif idade == 0:
             break
        else:
         print('Informe uma idade válida.')
    except Exception as e:
        print(f'Idade inválida: {e}')
   
mediaIdade = somaIdade / cont
print(f'A média de idade é: {mediaIdade}')