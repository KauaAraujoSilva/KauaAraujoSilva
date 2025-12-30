'''n = int(input('Digite o seu número: '))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end='')  # verde
        total += 1
    else:
        print('\033[31m', end='')  # vermelho

    print(f'{i}', end=' ')
    print('\033[m', end='')  # reset da cor

if total == 2:
    print('\nEle é primo')
else:
    print('\nEle NÃO é primo')'''
n = int(input('Digite o número: '))
divisores = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisores += 1

if divisores == 2:
    print('É primo')
else:
    print('Não é primo')


# diga se é ou nao um numero primo