i=0
Peaple = []
Listing = []
while True:
    Name = str(input('Nome: '))
    weight = float(input('Peso: '))
    
    Peaple.append(Name)
    Peaple.append(weight)

    Listing.append(Peaple[:])
    Peaple.clear()
    
    
    i+=1
   
    want_Continue = str(input('Deseja continuar[S/N]? ')).lower()
    if not want_Continue.startswith('s'):
        break
print(f'Você cadastrou {i} pessoas')
print(Listing)
print(weight*)