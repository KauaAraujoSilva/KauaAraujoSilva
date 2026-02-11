Lista = []
Acountant = 0
while True:
    Value = int(input('Digite um valor: '))
    Lista.append(Value)
    want_Continue = str(input('Deseja continuar[S/N]? ')).lower()
    Acountant +=1
    if not want_Continue.startswith('s'):
        break
print(sorted(Lista, reverse=True))
print(f'Foram digitados {Acountant} valores')
if 5 in Lista:
    print('O valor 5 estava na lista')
else:
    print('O valor 5 não foi encontrado')