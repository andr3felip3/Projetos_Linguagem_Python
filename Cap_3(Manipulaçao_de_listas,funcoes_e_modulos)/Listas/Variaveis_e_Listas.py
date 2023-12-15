
# Montar um Inventário

inventario=[] #cria uma lista dinamica
resposta="S"
while resposta == "S":
   inventario.append(input("Equipamento: "))
   inventario.append(float(input("Valor: ")))
   inventario.append(int(input("Numero Serial: ")))
   inventario.append(input("Departamento: "))
   resposta = input("Digite \"S\" para continuar: ").upper()
 # a entrada de dados do while fica sempre no fim do while

# Lista: nada mais é do que um conjunto de dados definidos por um identificador.
## []:define um objeto do tipo lista(ED).
## append(): acrescenta(insere) na lista
### lista dinâmica: o tamanho é definido conforme os dados são inseridos.
### lista estática: o tamanho já é predefinido antes da inserção.


# Exibe o Inventário

for elemento in inventario:
    print(elemento)