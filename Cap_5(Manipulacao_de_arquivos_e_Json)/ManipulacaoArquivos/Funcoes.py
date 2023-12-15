def perguntar():
    return input("\nO que deseja realizar?\n" +
              "<I> - Para inserir um usuario\n"+
              "<P> - Para pesquisar um usuario\n"+
              "<E> - Para excluir um usuario\n"+
              "<L> - Para Listar um usuário\n"
              ">:").upper()
#fim

def inserir(dicionario):
    print("\nInserção de usuarios")
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                                                   input("Digite a ultima data de acesso: "),input("Qual a ultima estacao acessada: ").upper()]
    salvar(dicionario)
#fim

def pesquisar(dicionario):
    chave = input("Informe o login do usuario que deseja pesquisar: ").upper()
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome......: " + lista[0])
        print("Ultimo acesso....: " + lista[1])
        print("Ultima estacao..: " + lista[2])
#fim

def excluir(dicionario):
    chave = input("Informe o login do usuario que deseja excluir: ").upper()
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Objeto excluido!")
#fim

def listar(dicionario):
    for (chave,valor) in dicionario.items():   #tupla
        print("Usuario.....")
        print("Login: ", chave)
        print("Dados: ", valor)

def salvar(dicionario):
    with open("bd.txt","a") as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

