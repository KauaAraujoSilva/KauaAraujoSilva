num = int(input('Digite o valor do seu numero: '))
print('\ndigite 1, Binario' '\ndigite 2, Octal' '\ndigite 3, Hexadecimal')
n = int(input('Digite qual opção você deseja: '))

if n == 1:
    print('Seu numero é {}, e em Binario é: {}.'.format(num, bin(num)[2:]))
elif n==2:
    print('Seu numero é {}, e em Octal é: {}.'.format(num, oct(num)[2:]))
elif n==3:
    print('Seu numero é {}, e em Hexadecimal é: {}.'.format(num, hex(num)[2:]))
else:
    print('Escolhar somente um numero de 1 à 3.')
#escolha qual base de conversão quer, sendo binario, octal e hexadecimal