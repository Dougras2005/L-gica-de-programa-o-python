class Aluno:


    def __init__(self, nome='', matricula='', notas=[]):
        self.nome = nome 
        self.matricula = matricula
        self.notas = notas
        self.conceito = ''
        self.media = 0
        self.resultado = ''

    def conceito_aluno(self):
        if self.media < 4:
            return 'E'
        elif self.media < 6:
            return 'D'
        elif self.media < 7.5:
            return  'C'
        elif self.media < 9.0:
            return 'B'
        else:
            return 'A'
        
    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'Aprovado'
        else:
            return 'Reprovado'
def impressao(aluno):
    print(f'Matrícula: {aluno.matricula}')
    print(f'Aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Media : {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

        
aluno1 = Aluno(nome='Gabriel', matricula='20231001', notas=[6, 4, 3])
aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
aluno1.conceito = aluno1.conceito_aluno()
aluno1.resultado = aluno1.resultado_aluno()

aluno2 = Aluno(nome='Douglas', matricula='20231001', notas=[8, 7, 9])
aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
aluno2.conceito = aluno2.conceito_aluno()
aluno2.resultado = aluno2.resultado_aluno()

impressao(aluno1)
print('')
impressao(aluno2)


