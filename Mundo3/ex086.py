Listagem = []
for i in range(0,3):
    for n in range(0,3):
        Value = int(input(f'Digite o valor[({n, i})]: '))
        Listagem.append(Value)
print(Listagem[0:3])
print(Listagem[3:6])
print(Listagem[6:9])