                        #criando variaveis
# Atribuição predefinida
inteiro = 2
flutuante = 2.5
logico = True
texto = "Texto de exemplo"

# Atribuição definida
nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionarios: "))
mediaMensalidade = float(input("Digite a media de mensalidade: "))
print(nome , "trabalha na empresa" , empresa) #concatenação de string(texto) com string
print("Possui: ",qtde_funcionarios, "funcionarios.") #concatenação de string com objeto
print("A media da mensalidade é de :",str(mediaMensalidade)) #concatenação de string com função(metodo)
print("============ Verifique os tipos de dados abaixo: ==============")
print("O tipo de dado da variavel [nome] é:",type(nome))
print("O tipo de dado da variavel [empresa] é", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é:", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é:", type(mediaMensalidade))

#Resumo
#dado: é um valor importante(compreensível) para o codigo | informação(conjunto de dados): é um conjunto de valores importantes(compreensiveis) para o usuário
# variavel: é um espaço reservado na memoria do computador para armazenar um dado  temporário
## Identificador de uma variavel: nada mais é do que o nome da variavel.
### Ele nao pode começar por numeros, nomes de comandos, letras maiusculas(so no meio) e caracteres especiais(so o "_" no meio)
# print("texto de exibição"): imprime(exibe) na janela de comandos um texto.
# input("texto de pergunta"): espera uma entrada de dados(texto) do usuario.
# int(input("texto de pergunta")): espera uma entrada de dados(texto) e converte em inteiro.
# float(input("texto de pergunta")): espera uma entrada de dados(texto) e converte em números flutuantes(usam casas decimais).
# type(): informa o tipo do objeto, a qual classe ele pertence.
# str(): converte um dado numerico em texto
# É recomendável que a concatenação seja feita pela virgula ",".
## ja que em alguns casos o "+" não funciona com funções.