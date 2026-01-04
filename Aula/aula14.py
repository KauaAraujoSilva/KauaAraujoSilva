'''c = 1
while c<=10:
    print(c)
    c+=1'''

'''v=1
while v != 0:
    v = int(input('Insira um numero: '))
print('Fim')'''

'''r = 'S'
while r =='S':
    v = int(input('Digite um valor: '))
    r = str(input('Quer continuar?(S/N): ')).upper()
print('Fim)'''
v = 1
pares = impar = 0
while v!=0:
    v = int(input( 'digite um valor: '))
    if v!=0:
        if v%2==0:
            pares+=1
        else:
            impar+=1
print(f'Teve {pares} numeros pares e {impar} numeros impares.')