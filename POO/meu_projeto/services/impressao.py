def impressao(produto):
        print(f'Codigo: {produto.codigo}')
        print(f'Nome: {produto.nome}')
        print(f'Quantidade em estoque: {produto.quantidade}')
        print(f'Preço : {round(produto.preco, 2)}')