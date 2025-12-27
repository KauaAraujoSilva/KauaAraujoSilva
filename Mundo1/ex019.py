import random
a1 = str(input("digite o nome do primeiro aluno: "))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o none do quarto aluno: '))
alunos = a1, a2, a3, a4
print('\033[32mo aluno escolhido foi o: {}\033[m'.format(random.choice(alunos)))