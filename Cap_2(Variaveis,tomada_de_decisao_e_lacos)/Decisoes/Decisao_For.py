tabuada = int(input("Digite um numero para exibir a tabuada: "))
print("Tabuada do numero",tabuada)
for valor in range(1,11,1):  #comando iterativo (para cada)
    print(str(tabuada) + "x" + str(valor) + "="+str((tabuada*valor)))

#range(x,y,z): metodo que define o inicio(x), fim(<y), incremento(z)
## range=faixa