
#---- Uma aplicação para poder receber informações de outros computadores ----#
## Cria-se uma aplicação servidora por meio do socket
### A aplicação abre uma porta de entrada(range de 0 a 65.535|maximo de maquinas que podem ser conectadas à aplicação)
#### Os clientes tem acesso a aplicação por meio dessa porta

#Na rede os computadores são identificados por meio do endereço ip ou um codinome predefinido(hostname)

import socket # biblioteca que permite pegar informações da rede
resp = "S"
while resp == "S":
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referente a url informada é: ",ip)
    resp = input("Digite <S> para continuar: ").upper()

# url: é o endereço mascarado(dominio) do site.
# ip: é o endereço real do site.
# gethostbyname(): pega o ip daquele dominio.

#--------------------------------------------------#

print(socket.getservbyname("domain")) # valor da porta para dominio
print(socket.getservbyname("http")) #valor da porta para acessar sites
print(socket.getservbyname("ftp")) #valor da porta para transferencia de arquivo
#porta: é o mecanismo de entrada para ter acesso ao serviço do protocolo
