frase = str(input('Digite algo: ')).upper().strip()
print('No que foi digitado, existe {} letras "A"'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição: {}'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na posição: {}'.format(frase.rfind('A')+1))

#quantas vzz aparece letra A
#em que posição aparece na primeira e na ultima vez