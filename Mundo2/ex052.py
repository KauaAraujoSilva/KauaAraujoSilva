n = int(input('Digite o seu numero: '))
total = 0
for i in range (1, n+1):
    if n%i==0:
        total+=1
if total==2:
    print('É PRIMO')
else:
    print('Não é primo')
# diga se é ou nao um numero primo