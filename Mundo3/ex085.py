lista = []
for n in range(7):
    Value = int(input(f'Digite o {n}o. valor: '))
    par = Value%2==0
    impar = Value%2!=0
    if par:
        lista.append(Value)
        print(par)
    if impar:
        lista.append(Value)
print(par)
print(impar)