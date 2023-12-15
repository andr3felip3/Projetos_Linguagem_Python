baseDados = []
with open("iris.data","r") as arquivo: # abre o arquivo con intenção de leitura
    for registro in arquivo.readlines(): #posiciona o indice sobre cada registro do arquivo

        baseDados.append(registro.split(","))
        # cada registro poscionado é adicionaddo na lista base de dados em formato de lista
        # sem o caractere virgula.

print(baseDados)

print(baseDados[0][0]) # acessa elemento da primeira posição e da primeira coluna

print(float(baseDados[0][0])+float(baseDados[0][1])) # soma esses elementos