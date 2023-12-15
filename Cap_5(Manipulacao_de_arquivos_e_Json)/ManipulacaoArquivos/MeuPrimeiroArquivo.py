
#============================================================================================#

                                #----- UMA ABORDAGEM -----#

#----------------------------------------------
arquivo = open("primerioArquivo.txt","w")
# apelido = open("nome do arquivo","intenção"): abre um arquivo
## apelido: é a variavel que guarda o arquivo
### intenção:
# 'w':(cria e escreve | se ja existe o arquivo, escreve de novo(sobrescreve)),
# 'r':(leitura | o arquivo ja deve existir),
# 'a':(acrescentar | o arquivo ja deve existir),
# 'x':(torna arquivo não editavel).

arquivo.write("Meu primeiro arquivo ! Ai que festa!")
# write("texto"): para escrever no arquivo

arquivo.close()
# close(): fecha o arquivo, deve ser fechado para salvar as alterações

#============================================================================================#


                                #----- OUTRA ABORDAGEM -----#

#------------------------------------------------
# Escrita #

with open("primeiroArquivo.txt","a") as arquivo:
    arquivo.write("\nHakuna Matata!!")

#whith "operação" as "Apelido": usando essa abordagem não precisa dar o close()

#-------------------------------------------------

#Leitura #

with open("primeiroArquivo.txt","r") as arquivo: # chama o arquivo com intenção de leitura
    conteudo = arquivo.read() # carrega o conteudo do arquivo na variavel conteudo.
    print(conteudo)

#read(): faz leitura completa do arquivo
#readline(): faz leitura somente da primeira linha

with open("primeiroArquivo.txt","r") as arquivo: # exibe o conteudo linha por linha
    for linha in arquivo.readlines():
        print(linha)

#----------------------------------------------------

#============================================================================================#

                                        # RESUMINDO #
##############################################
# # Utilizando uma abordagem #
#
#     *Escrita:
# apelido = open("nome do arquivo.txt", "operação")
# apelido.write("Texto a ser escrito")
# apelido.close()
#
#     *Leitura:
# apelido = open("nome do arquivo", "operação")
# conteudo = apelido.read()
# apelido.close()
#
#     *Leitura linear
# apelido = open("nome do arquivo","operacao")
#    for linha in apelido.readlines()
#      print(linha)
# apelido.close()
###############################################
# # Utilizando outra abordagem #
#
# *Escrita:
# with open("nome do arquivo", "operação")
#     apelido.write("Texto a ser escrito")
#
#     *Leitura:
# with open("nome do arquivo", "operacao")
#     conteudo = apelido.read()
#
#     *Leitura linear:
# with open("nome do arquivo", "operacao") as apelido
#     for linha in apelido.readlines():
#         print(linha)