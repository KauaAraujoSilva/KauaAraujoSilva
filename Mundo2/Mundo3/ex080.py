Lista = []
for n in range(5):
    Value = int(input('Digite um valor: '))
    if n == 0 or Value > Lista[-1]:
        Lista.append(Value)
    else:
        Position = 0 
        while Position < len(Lista):
            if Value <= Lista[Position]:
                Lista.insert(Position, Value)
print(f'O valores digitados foram: {Lista}')