lista = [[],[]]
for n in range(7):
    Value = int(input(f'Digite o {n}o. valor: '))
    if Value%2==0:
        lista[0].append(Value)
    if Value%2!=0   :
        lista[1].append(Value)
Lista_ordenada = sorted(lista)
print(f'Os valores pares sao: {Lista_ordenada[0]}')    
print(f'Os valores impares sao: {Lista_ordenada[1]}')    