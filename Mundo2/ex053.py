frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
# print(inverso, junto)
if inverso == junto:
    print('Essa frase é um polidromo')
else:
    print('Não é um polidromo')
# leia frase qualquer e diga se é um palidromo(desconsidere espaços )