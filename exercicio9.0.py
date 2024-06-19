sigla = input('Digíte a sigla dos estado: (RJ,SP,GO,etc.)')
sigla = sigla.upper()

if sigla == 'RJ':
    print(f'O estado da sliga {sigla} é Rio de Janeiro.')
elif sigla == 'SP':
    print(f'O estado da sliga {sigla} é São Paulo.')
elif sigla == 'GO':
    print(f'O estado da sliga {sigla} é Goiás.')
else:
    print('Erro! Digíte a sigla informada!')