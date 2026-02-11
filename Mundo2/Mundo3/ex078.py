lista = []
for i in range(5):
    n = int(input(f'Digite o valor para a posição {i}: '))
    lista.append(n)
print()
menor = min(lista)
maior = max(lista)
print(f'A lista foi: {lista}')
print()
print(f'O menor valor da lista foi: {menor}')
for i, v in enumerate(lista):
    if v == menor:
        print('O valor esta na posição: ', i)
print()
print(f'O maior valor da lista foi: {maior}')
for i, v in enumerate(lista):
    if v == maior:
        print('O valor esta na posição: ', i)