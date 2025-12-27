medida = int(input("Digite o valor em metros: "))
km = medida/1000
ham = medida/100
dam = medida/10
dm = medida*10
cm = int(medida * 100)
mm = int(medida * 1000)
print("Seu valor em kilometros é: {}, em hectometros é: {}," \
" em decametro é {} e em metros é: {}, em decimetros é {}, em centimetros é: {} e em milimetros é: {}".format(km, ham, dam, medida, dm, cm, mm))