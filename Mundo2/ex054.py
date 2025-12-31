from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for i in range (1, 8):
        nasc = int(input('Em que ano a pessoa nasceu?: '))
        idade = atual - nasc
        if idade>=21:
                maioridade+=1
        else:
                menoridade+=1
print(f'Tivemos {maioridade} pessoas maior de idade')
print(f'Tivemos tambem, {menoridade} pessoas menor de idade')
# leia ano de nasc. de 7 pessoas, e mostre se atingiu a maioridade(21anos)