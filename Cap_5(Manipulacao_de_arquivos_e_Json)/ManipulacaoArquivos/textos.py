# A string(texto): nada mais é do que a mistura de uma lista com a tupla
# Armazena um conjunto de dados
# Os dados não podem ser modificados

texto = "Leia e Han Solo"
#        012345678901234 : posições das letras na lista
print(texto[0:4])
print(texto[7:]) # ":" se deixar só dois pontos vai até o final
print(texto[::-1]) # inverte a string

#exemplo teste
print(texto[0:4:2])
#começa da posição "0"
#irá acessar "4" posições
#percorre a primeira e acessa a segunda

#---- Formato de movimentação na string ----#
# string[x:y:z]
## x: posição inicial
## y: posições que serão percorridas
## z: passo (intervalo de acesso das posiçoes)