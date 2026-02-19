from random import sample
Mega_Sena = []
Quantidade_de_jogos = int(input('Quantos jogos você deseja sortear? '))
print(f'SORTEANDO {Quantidade_de_jogos} JOGOS')
for n in range(1, Quantidade_de_jogos+1):
    Value = sample(range(1,60), k=6)
    print(f'Jogo {n}: {Value}')
print('Boa sorte!')