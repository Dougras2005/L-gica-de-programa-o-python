class Produto:


    def __init__(self, nome='',codigo='', preco='', quantidade=[]):
        self.nome = nome 
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
        
  
Produto = []
while True:
    quantidade = []
    codigo = input('Digite a codigo: ')
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço do produto: '))

    sair = input('Digite s para sair ou enter para continuar: ')

    if sair.upper() == 'S':
        break
