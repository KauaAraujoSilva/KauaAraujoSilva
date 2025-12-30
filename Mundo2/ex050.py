s=0
c=0
for i in range(1,7):
    n = int(input(f'Digite o {i}° numero: '))
    if n%2==0:
        s+=n
        c+=1
print(f'A soma de {c} numeros pares, é igual à: {s}')
# leia 6 numeros int e mostre a soma somente de num pares, se o valor for impar, desconsidere