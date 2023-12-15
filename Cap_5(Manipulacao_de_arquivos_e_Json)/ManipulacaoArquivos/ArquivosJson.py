import json
#========================== Manipulação de arquivos Json ==================#

# #--- Arquivo json ---#
# # É uma notação do javascript
# # É semelhante a um dicionario de dados
#
#--------- Ler um aquivo Json -----------------------#

with open("bd.json","r") as arq_json: # abre o arquivo e coloca o apelido de arq_json
    dicionario = json.load(arq_json) # carrega seu conteudo na variavel dicionairio
    for chave,dados in dicionario.items(): # exibe o conteudo em forma de tupla
        print(chave+"|"+str(dados))

#-------- Escrever(gravar) em um aquivo Json ---------#

dicionario ={
  "CHAVE":["CHAVES DO 8", "14/04/2017", "RECEP_01"],
  "QUICO": ["QUICO FLORES", "24/04/2017", "RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_03"]
} # Estrutura de dados para colocar no arquivo json

with open("bd1.json","w") as json_file: #criar arquivo com intenção de escrita
    json.dump(dicionario,json_file) # grava a ed no arquivo json
# dump("estrutura de dados","arquivo json")