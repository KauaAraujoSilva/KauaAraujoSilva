Listagem = []
Maior_valor_segunda_coluna = []
Par = Terceira_coluna = 0
for i in range(0,3):
    for n in range(0,3):
        Value = int(input(f'Digite o valor[{i,n}]: '))

        if Value%2==0:
            Par += Value
        if n ==2:
            Terceira_coluna += Value
        if i ==1:
            Maior_valor_segunda_coluna.append(Value)
        Listagem.append(Value)
print(Listagem[0:3])
print(Listagem[3:6])
print(Listagem[6:9])
print(f'A soma dos valores pares foi igual a: {Par}')
print(f'A soma dos valores da terceira coluna foi: {Terceira_coluna}')
print(f'O maior valor da segunda coluna foi: {max(Maior_valor_segunda_coluna)}')