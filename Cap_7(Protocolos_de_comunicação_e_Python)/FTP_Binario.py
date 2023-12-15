
from ftplib import *

ftp = FTP('ftp.ibiblio.org') #cria conexao ftp
print(ftp.getwelcome()) #informa status da conexao
ftp.login() #define um login
ftp.cwd('/pub/linux/logos/pictures') #define esse diretorio para trabalho
with open ('pai_do_linux.jpg', 'wb') as arq: #cria arquivo binario
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write) #llê informação e coloca no arquivo binario
ftp.quit() #fecha conexao ftp

#retrbinary('arquivo a ser lido','local que ficara armazenado')