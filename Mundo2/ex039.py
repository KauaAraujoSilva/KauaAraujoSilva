from time import localtime
idade = int(input('Digite a sua idade: '))
temp = localtime().tm_year
print('Você nasceu em {}.'.format(temp - idade))
if idade<=17:
    print('Ainda falta {} anos para você se alistar.'.format(18 - idade))
elif idade<=18:
    print('Você deve se alistar imediatamente!')
else:
    print('Você ja deveria ter se alistado!')
    print('Você excedeu {} anos do tempo de alistamento.'.format(idade-18))

'''print('Ainda falta {} para se alistar.'.format(tempo))'''
#leia ano e informe idade, mostre, se ele vai se alistar, se ja é hora, ja passou. 
#deve mostrar temp q falta/excedeu