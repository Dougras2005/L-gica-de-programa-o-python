class Aluno:
    nome = ''
    matricula = ''
    notas = []
    conceito = ''
    media = 0
    resultado = ''

    def conceito(self):
        if self.media < 4:
            self.conceito = 'E'
        elif self.media >= 40 < 60:
            self.conceito = 'D'
        elif self.media >= 60 < 75:
            self.media = 'C'
        elif self.media >= 75 < 90:
            self.conceito = 'B'
        elif self.media >= 90:
            self.conceito = 'A'
        
    
aluno1 = Aluno()
aluno1.nome = 'Douglas'
aluno1.matricula = '202310001'
aluno1.notas = [8, 7, 9]

aluno1.media = sum(aluno1.notas) / len(aluno1.notas)

print(f'Matrícula: {aluno1.matricula}')
print(f'Aluno: {aluno1.nome}')
print(f'Notas: {aluno1.notas}')
print(f'Media : {round(aluno1.media, 1)}')