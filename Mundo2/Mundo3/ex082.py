Lista = []
Pair = []
Odd = []
while True:
    Value = int(input('Digite um numero: '))
    want_Continue = str(input('Deseja continuar[S/N]? ')).lower()
    Lista.append(Value)

    if not want_Continue.startswith('s'):
        break
for i, v in enumerate(Value):
    if v%2==0:
        Pair.append(v)
    elif v%2==1:
        Odd.append(v)
print(f'A lista formada foi: {Lista}')
print(f'Os valores PARES foram: {Pair}')
print(f'Os valores IMPARES foram: {Odd}')