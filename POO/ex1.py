class Aluno:
    nome = ''
    matricula = ''
    notas = []
    conceito = ''
    media = 0
    resultado = ''

    def conceito_aluno(self):
        if self.media < 40:
            self.conceito = 'E'
        elif self.media < 60:
            self.conceito = 'D'
        elif self.media < 75:
            self.media = 'C'
        elif self.media < 90:
            self.conceito = 'B'
        else:
            self.conceito = 'A'

        
    
aluno1 = Aluno()
aluno1.nome = 'Douglas'
aluno1.matricula = '202310001'
aluno1.notas = [8, 7, 9]

aluno1.media = sum(aluno1.notas) / len(aluno1.notas)

aluno1.conceito = aluno1.conceito_aluno()
print(f'Matrícula: {aluno1.matricula}')
print(f'Aluno: {aluno1.nome}')
print(f'Notas: {aluno1.notas}')
print(f'Media : {round(aluno1.media, 1)}')
print(f'Conceito: {aluno1.conceito_aluno}')