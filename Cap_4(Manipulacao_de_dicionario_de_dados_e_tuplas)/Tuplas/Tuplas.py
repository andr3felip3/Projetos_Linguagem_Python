# Tupla: é um tipo de estrutura de dados imutável(não muda)
## serve só para consulta e exibir dois dados combinados(pares)
## como se fosse uma informção divida em duas partes
### melhor do que exibir tudo em uma linha só
#### Tambem pode ser utilizada como chave
# (): define um objeto do tipo tupla

usuarios = {}
emails = ["xpto@xyz.com","xkcd@phd.com"]

tupla = list(enumerate(emails)) # o list concatena numero e email formando uma tupla


for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1]) # exibe os itens(emails) dentro da tupla de acordo com indice(chave)
    usuarios[tupla[chave]] = [input("Digite o nome: "),input("Digite o nivel: ")] # insere dados de acordo com o indice no dicionario

# tupla[x][y]:consulta a tupla, x(nºcoluna da tupla) | y(nºlinha da tupla)

for chave, dado in usuarios.items(): #tupla
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nivel....:", dado[1])

# (chave,dado): é uma tupla de indices que cada indice exibe dois valores(numero,texto).