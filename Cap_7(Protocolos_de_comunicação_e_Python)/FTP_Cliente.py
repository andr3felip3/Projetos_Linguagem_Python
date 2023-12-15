
from ftplib import * #importa todos os metodos da biblioteca ftp
ftp = FTP('ftp.ibiblio.org') #cria um objeto de conexão com cliente pelo argumento(dominio do cliente)
print(ftp.getwelcome()) #uma mensagem de confirmação da conexao
usuario = input("Digite o usuario: ")
senha  = input("Digite a senha: ")
ftp.login(usuario,senha) #estabelece um login para essa conexão
print("Diretorio atual de trabalho: ",ftp.pwd()) #informa qual o diretorio atual do cliente
ftp.cwd('andre') #muda para o diretorio pub
#pwd():informa diretorio atual
#cwd(x):muda p/ diretorio x
print("Diretorio corrente: ",ftp.pwd())
ftp.quit() #fecha conexão
