
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

# Coloca o dado a ser buscado dentro de uma variavel auxiliar (va)
## No caso vai ser o nome de um equipamento
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for indice in range(0,len(equipamentos)): # Percorre a lista equipamentos
    if busca == equipamentos[indice]: # compara a va com os itens da lista equipamentos
        # Exibe se achar o dado em questão
        print("Valor..:", valores[indice])
        print("Serial.:", seriais[indice])