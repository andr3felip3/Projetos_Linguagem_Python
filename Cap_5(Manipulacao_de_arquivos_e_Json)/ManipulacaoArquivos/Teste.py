
with open("D:/Biblioteca/Downloads/testeArquivo.txt","w") as arquivo:
    arquivo.write("Este é um teste de arquivo texto em diretorio diferente do padrão")

with open("D:/Biblioteca/Downloads/testeArquivo.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
