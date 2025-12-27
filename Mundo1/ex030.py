'''num = int(input('Digite o numero: '))
if (num/2) % 1:
    print('É impar')
else:
    print('É par')'''
#leia um num inteiro, mostre se é impar ou par

num = int(input('Digite um numero qualquer: '))
resultado = num % 2
if resultado == 0:
    print('É PAR')
else:
    print('É IMPAR')