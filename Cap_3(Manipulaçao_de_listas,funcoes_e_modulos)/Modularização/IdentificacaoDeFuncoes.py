# Codigo monolítico: todas as instruções do codigo estão em uma parte só,sequencialmente.
## Modularização: as instruções estão divididas em blocos(modulos/funções) que podem ser acessados em qualquer situação.


# Esse é o arquivo que vai conter as funções !!
## Sendo que esse arquivo necessita ser importado por outro para elas serem utilizaveis.



##-- Função --##

#Para criar uma função:
## def 'nome da função'('parametro'):
### parametro: é o tipo de dado que ela tem que receber.
# Para chamar uma função
## 'nome da função'('argumento')
### argumento: é o dado que to enviando.


def preencherInventario(lista): # Define uma função que recebe uma lista via parametro
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "), float(input("Valor: ")),
                       int(input("Numero Serial: ")), input("Departamento: ")]
        lista.append(equipamento)  # Coloca a lista equipamento dentro da lista inventario
        resp = input("Digite \"S\" para continuar: ").upper()
# fim

def exibirInventario(lista):
    for elemento in lista:
        print("\nNome.....:", elemento[0])
        print("Valor....:", elemento[1])
        print("Serial.....:", elemento[2])
        print("Departamento.....:", elemento[3])
# fim

def localizaPorNome(lista):
    busca = input("Digite o \"NOME\" do equipamento que deseja buscar: ")

    for elemento in lista:  # para percorrer
        if busca == elemento[0]:
            print("\nValor..:", elemento[1])
            print("Serial.:", elemento[2])
# fim

def depreciacaoPorNome(lista,porc):
    depreciacao = input("Digite o \"NOME\" do equipamento que será depreciado: ")

    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)  # altera o valor do dado
            print("Novo valor: ", elemento[1])
# fim

def excluirPorSerial(lista):
    serial = int(input("Digite o \"SERIAL\" do equipamento que será excluido: "))

    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)  # remove um item da lista inventario a partir do elemento
    return "Itens excluidos"
# fim

def resumirValores(lista):
    valores = []

    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos e de: ", sum(valores))
# fim
