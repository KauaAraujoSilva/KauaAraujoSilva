import random
from time import sleep
rnd = random.randint(0,5)
num = int(input('Escolha um numero de 0 até 5: '))
print('PROCESSANDO...')
sleep(3)
print(num)
if num == rnd:
    print('PARABENS, VOCÊ ACERTOU O NUMERO.')
else:
    print('VOCE ERROU!')
print('O numero escolhido  foi: {}'.format(rnd))

#Tente advinhar o numero que o computador escolheu