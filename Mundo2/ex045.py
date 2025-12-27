import random
from time import sleep
rnd = random.randint(1,3)
# itens = ('pedra', 'papel', 'tesoura')
# print('O computador escolheu: {}.'.format(itens[rnd]))
# dava pra fazer desse jeito acima, em vez de declarar cada numero
print('Escolha um para jogar!')
print('''
    PEDRA = [ 1 ] 
    PAPEL = [ 2 ] 
    TESOURA = [ 3] ''')
n = int(input('Digite um numero: '))
if n==1:
    print('Você escolheu pedra')
if n==2:
    print('Você escolheu papel')
if n==3:
    print('Você escolheu tesoura')

elif n!= 1 and n!=2 and n!=3:
    print('Esse numero não pode ser escolhido')
    print('Você perdeu!')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if rnd==1:
    print('Computador escolheu pedra')
if rnd==2:
    print('Computador escolheu papel')
if rnd==3:
    print('Computador escolheu tesoura.')

if n==1 and rnd==1 or n==2 and rnd==2 or n==3 and rnd==3:
    print('EMPATE, jogue novamente')
elif n==1 and rnd==3 or n==2 and rnd==1 or n==3 and rnd==2:
    print('Você venceu!')
elif rnd==1 and n==3 or rnd==2 and n==1 or rnd==3 and n==2:
    print('Computador venceu!')


# crie um programa pra jogar jokempo
