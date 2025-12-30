pritermo = int(input('Digite o valor do primeiro termo: '))
razão = int(input('Digite o valor da razão da P.A.: '))
decimo = pritermo + (10 - 1)*razão
# for i in range(pritermo, decimo+razão, razão):
#         print(f'{i}', end='-')
# print('FIM')
for n in range(1,11):
    print(f'\033[32m{n}° termo: {pritermo + (n-1)*razão}\033[m')

# an=a1 +(n-1)*r
# leia 1° termo e a razãode uma P.A.. mostre os 10 primeiros termos