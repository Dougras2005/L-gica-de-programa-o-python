numeros = []
indice = 0
maior = 0
indice = 0
numero = int(input('Digite um numero: '))
numeros.append(numero)
maior = numero

for n in range(1,10):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if maior< numero:
        maior = numero 
        indice = n 
    
print(f'Lista dos números: {numeros}.')
print(f'Maior número: {maior} - seu índice é: {indice}.')