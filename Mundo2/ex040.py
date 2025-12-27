n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
med = (n1 + n2)/2
print('SUA MEDIA É DE {}'.format(med))
if med<5:
    print('REPROVADO')
elif med>=5 and med<=6.9:
    print('RECUPERAÇÃO')
elif med>7:
    print('APROVADO')
#calcule a media, leia 2 notas, <5=reprovado,5-6.9=recuperação,>7=aprovado