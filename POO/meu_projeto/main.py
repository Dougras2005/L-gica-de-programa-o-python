
from models.produto import Produto


def impressao(produto):
        print(f'Codigo: {produto.codigo}')
        print(f'Nome: {produto.nome}')
        print(f'Quantidade em estoque: {produto.quantidade}')
        print(f'Preço : {round(produto.preco, 2)}')
     
def cadastro():
    codigo = input('Digite a codigo: ')
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço do produto: '))
        
    produto = Produto(nome, codigo, preco, quantidade)

    return produto

def pesquisa(produtos):
    print('###### Pesquisa do Produto ######')
    achei = None
    busca = input('Digite o codigo do produto que deseja ver os dados: ')
    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            break
    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado!')

def lista_produtos(produtos):
    print('\n ###### Lista de Produto ######')
    for produto in produtos:
        impressao(produto)
        print('')

def venda_produto(produtos):
    print('###### Venda de Produto ######')
    busca = input('Digite o codigo do produto que deseja ver os dados: ')
    achei = None 
    perc = None
    quant = 0
    estoque = True
    valor_desconto = 0.0
    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            quant = int(input('Digite a quantidade: '))
            if quant > produto.quantidade:
                estoque = False
                break
            produto.quantidade -= quant
            perc = float(input('Digite o percentual do desconto: '))
            valor_desconto = produto.desconto(perc)
            break
    if achei is not None and estoque:
        impressao(achei)
        print(f'Preço com desconto: {valor_desconto}')
        print(f'Total: {valor_desconto * quant}')
    elif not (estoque):
        print(f'Estoque insuficiente: {produto.quantidade}')
    else:
        print('Produto não encontrado!')

def reajuste_produto(produtos):
    print('###### Venda de Produto ######')
    achei = None
    busca = input('Digite o codigo do produto que deseja ver os dados: ')
    perc = float(input('Digite o percentual do desconto em %: '))
    preco_reajustado = 0.0
    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            preco_reajustado = produto.reajuste(perc)
            produto.preco = preco_reajustado
            break
    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado!')

    

    

  
produtos = []
while True:
    opcao = int(input('Escolha opção desejada \n'
                  '\n1- Para cadastrar produto'
                  '\n2- Para pesquisar produto'
                  '\n3- Para impressão da lista de produtos'
                  '\n4- Para venda do produto'
                  '\n5- Para reajuste: '
                  ))


    if opcao == 1:
        produtos.append(cadastro())
    elif opcao == 2:
        pesquisa(produtos)
    elif opcao == 3:
        lista_produtos(produtos)
    elif opcao == 4:
        venda_produto(produtos)
    elif opcao == 5:
        reajuste_produto(produtos)
    else:
        print('Opção inválida')


    sair = input('Digite s para sair ou enter para continuar: ')
    if sair.upper() == 'S':
        break









