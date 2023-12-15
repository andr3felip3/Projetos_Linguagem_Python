
# Dicionario de dados: é quando um dado especifico e unico,serve
# como referencia(chave) pra consultar o conjunto de dados
# que está associado a ele. Ex: cpf.

##Lista: uma estrutura de dados linear(sequencial) | repete os dados a cada inserção, pois necessita de uma varredura na lista pra encontrar o item.
##Dicionario de dados: uma estrutura de dados não linear(escalonavel) | só atualiza os dados cada inserção, pois pode acessa-lo diretamente.


  # É recomendavel nome das estruturas estejam no plural.
usuarios = {} # cria um dicionario de dados vazio
# {}: define um objeto do tipo dicionario(ED)
print(usuarios)

# Dentro do dicionario, o que tiver antes dos ":" é a chave e o que tiver depois é o registro associado a chave.

 # Definindo dados de maneira antecipada no dicionario
usuarios = {"chaves":["Chaves do 8","24/12/2017","Recp_01"],
            "quico":["Quico das flores","20/12/2017","Raiox_03"]}

# Dicionario = {'chave':['registro']}

print(usuarios)

 # Acrescentando(inserção) dados no dicionario
usuarios["florinda"] = ["Dona florinda","24/12/2017", "Raiox_01"]
# dicionario['chave'] = ['Registro']
print(usuarios)

print("###---###")
print(usuarios.get("quico"))
# get(): serve para buscar um registro por meio de sua chave





# items(): retorna dados combinados(tuplas) entre chave e registro.
# values(): retorna somente o registro.
# keys(): retorna somente as chaves.
# has_key():  vefiica se chave ta dentro do dicionario ou não
# clear(): esvazia completamente o dicionario
# popitem(): a cada execução resultará na remoção do item do dicionario


















