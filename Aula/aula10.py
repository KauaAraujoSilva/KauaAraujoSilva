'''tempo = int(input('Digite quanto tempo tem o seu carro: '))
print('carro novo' if tempo <=3 else 'carro velho')
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')'''
#quanto tempo tem o seu carro

''''nome = str(input('Qual o seu nome?:  '))
if nome == 'Kauã':
    print('Que nome lindo!')
else:
    print('Que nome comum...')
print('Ola {}, bem vindo!'.format(nome))'''
#qual o seu nome
 
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2)/2
print('A sua media foi: {:.1f}'.format(media))
if media >=6.0:
    print('Parabéns. você passou!')
else:
    print('Você reprovou.')
#sistema de notas escolares