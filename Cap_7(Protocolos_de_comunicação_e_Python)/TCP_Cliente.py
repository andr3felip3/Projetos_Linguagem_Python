
from socket import * #Este tipo de import pega todos os metodos da biblioteca

servidor = "127.0.0.1" #endereço que vou conectar
porta = 43210 #porta que vou entrar
msg = bytes(input("Digite algo: "), 'utf-8') #mensagem que vou mandar para o servidor
#---------------------- Configuração do cliente ----------------------#
obj_socket = socket(AF_INET,SOCK_STREAM) #cria a aplicação TCP
obj_socket.connect((servidor,porta)) #eexecuta como aplicação cliente
obj_socket.send(msg) #envia uma mensagem pro servidor
resposta = obj_socket.recv(1024) #recebe uma mensagem(pacote) do servidor
print("Recebemos: ",resposta)
obj_socket.close() #fecha conexão para liberar a porta