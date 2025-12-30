s = 0
c = 0
for i in range(1,501, 2):
    if i%3==0:
        c += 1
        s += i
print(f'A soma dos {c} valores é de: {s}')
# soma de 1 ate 500 de num multiplo de 3 e impares