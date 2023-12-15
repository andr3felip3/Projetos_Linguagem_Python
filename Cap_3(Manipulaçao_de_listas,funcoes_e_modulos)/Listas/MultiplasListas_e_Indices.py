
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

#Insere dados em cada uma das listas

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(input("numero serial: "))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

#Exibe as listas

for indice in range(0,len(equipamentos)): #um contador (indice) q vai de 0 ate o nmr de itens da lista equipamentos
    print("\nEquipamento..:", indice+1) #exibe o valor do contador naquela rotina
    # exibe os itens de cada lista definidos por sua posição em relação ao contador
    print("Nome.......:",equipamentos[indice])
    print("Valor......:",valores[indice])
    print("Serial.....:",seriais[indice])
    print("Departamento....:",departamentos[indice])
#obs: para acessar o contador de um comando de iteração usa-se o colchete
