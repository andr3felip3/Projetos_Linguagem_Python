
from ftplib import * # biblioteca que permite trabalhar com o protocolo ftp
ftp = FTP('ftp.ibiblio.org')
# FTP(dominio ftp): cria um objeto do cliente alvo da conexao
print(ftp.getwelcome()) # uma mensagem de status da conxeão do cliente com minha aplicação
ftp.quit()

# Mensagem: 220 ProFTPD Server | quer dizer exito na conexão e pode realizar a transferencia de arquivos