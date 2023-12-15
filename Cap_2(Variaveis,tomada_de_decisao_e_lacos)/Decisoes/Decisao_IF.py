nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infeccontagiosa = input("Suspeita de doença infeccontagosa?: ").upper()
if idade >= 65:   #condicional (se)
    print("O paciente", nome, "Possui atendimento prioritario!")  #decisão
# DECISÂO ENCADEADA
elif doenca_infeccontagiosa == "SIM": #condicional (senão se)
    print("O paciente", nome ,"deve ser direcionado para sala de espera reservada")
else:    #condicional (senão)
    print("O paciente", nome, "Não possui atendimento prioritário")

print("fim") # sempre será impresso ja que está no mesmo nivel do if/else


# as subrotinas no python se iniciam por dois pontos ":"
## sendo que só vai ser executado aquilo que estiver seguido dele (na linha abaixo)
### Em um paragrafo afastado(indentação) dele.
#upper(): trasnforma um texto em caixa alta.