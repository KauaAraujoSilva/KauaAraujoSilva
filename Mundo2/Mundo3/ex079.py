lista = []
while True:
    Value = int(input('Digite um Valor: '))
    if not Value in lista:
        lista.append(Value)
    else:
        print('O Valor ja esta adicionado.')
    want_Continue = str(input('Quer continuar[S/N]? ')).lower()
    if want_Continue.startswith('s'):
        continue
    else:
        break
print(f'Voce digitou os valores: {sorted(lista)}')