
# Esse é o arquivo que vai chamar as funções!!

from Projetos.Modularização.IdentificacaoDeFuncoes import* # importa um arquivo de um diretorio
## ex: from 'diretorio'.'subdiretorio'.'arquivo' import *

minhaLista = []

print("\nPreenchendo")
preencherInventario(minhaLista)


print("\nExibindo")
exibirInventario(minhaLista)

print("\nPesquisando")
localizaPorNome(minhaLista)

print("\nAlterando")
depreciacaoPorNome(minhaLista,20)

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("\nResumindo")
resumirValores(minhaLista)
