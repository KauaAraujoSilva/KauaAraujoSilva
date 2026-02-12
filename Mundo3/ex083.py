Value = str(input('Digite a sua expreção: '))
Open = Value.count('(')
Closed = Value.count(')')
if Open == Closed:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta INCOMPLETA')