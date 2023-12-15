# Depreciação e exclusão
inventario=[]
resposta = "S"
while resposta == "S":
    equipamento = [input("Equipamento: "), float(input("Valor: ")),
                   int(input("Numero Serial: ")), input("Departamento: ")]
    inventario.append(equipamento) #Coloca a lista equipamento dentro da lista inventario
    resposta = input("Digite \"S\" para continuar: ").upper()

# posiciona o indice elemento em cada sublista onde pode consultar qualquer item dela.
## isso seria uma forma de manipular(percorrer) as sublistas(equipamentos) dentro da lista inventario
for elemento in inventario:
    # Exibições para melhorar a compreensão
    print("Nome.......:", elemento[0])
    print("Valor......:", elemento[1])
    print("Serial.....:", elemento[2])
    print("Departamento....:", elemento[3])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for elemento in inventario:  # para percorrer
    if busca == elemento[0]:
        print("Valor..:", elemento[1])
        print("Serial.:",elemento[2])

depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")

for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ",elemento[1])
        elemento[1] = elemento[1] * 0.9  # altera o valor do dado
        print("Novo valor: ", elemento[1])


serial = int(input("\nDigite o serial do equipamento que será excluido: "))

for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento) #remove um item da lista inventario a partir do elemento

for elemento in inventario:
    print("Nome.......:", elemento[0])
    print("Valor......:", elemento[1])
    print("Serial.....:", elemento[2])
    print("Departamento....:", elemento[3])

valores = []

for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa: ",max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos e de: ", sum(valores))

# max(): pega o item de maior valor de uma lista
# min(): pega o item de menor valor de uma lista
# sum(): faz a soma dos valores dos itens de uma lista


