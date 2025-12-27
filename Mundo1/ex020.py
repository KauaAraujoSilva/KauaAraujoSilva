import random
a1 = input('DIGITE O NOME DO PRIMEIRO ALUNO: ')
a2 = input("DIGITE O NOME DO SEGUNDO ALUNO: ")
a3 = input("DIGITE O NOME DO TERCEIRO ALUNO: ")
a4 = input('DIGITE O NOME DO QUARTO ALUNO: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista) #shuffle é embaralhar
print('a ordem de apresentação sera de {}'.format(lista))