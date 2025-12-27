from time import localtime
idade = int(input('Digite a sua idade: '))
ano = localtime().tm_year
print('Você nasceu no ano de {}'.format(ano-idade), end = ' ')
print('então você tem {} anos'.format(idade))
if idade <=9:
    print('Sua categoria é: \033[32mMIRIM\033[m')
elif idade<=14:
    print('Sua categoria é: \033[32mINFANTIL\033[m')
elif idade<=19:
    print('Sua categoria é: \033[32mJUNIOR\033[m')
elif idade<=20:
    print('Sua cateogira é: \033[32mSENIOR\033[m')
elif idade>20:
    print('Sua categoria é: \033[32mMASTER\033[m')
#ano do atleta e mostre a sua categoria de acordo com a idade
# colocar ano atual