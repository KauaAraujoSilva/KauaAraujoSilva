primeiro = int(input('Digite o primeiro valor: '))
razão = int(input('Digite o valor da razão: '))
decimo = primeiro + (10-1)*razão
for i in range(primeiro, decimo+1, razão):
    print(i, end=' - ')
print('Fim')
# an=a1 +(n-1)*r
# leia 1° termo e a razãode uma P.A.. mostre os 10 primeiros termos