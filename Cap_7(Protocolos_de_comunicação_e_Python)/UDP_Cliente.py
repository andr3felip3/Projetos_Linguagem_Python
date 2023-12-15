from socket import *
#---------------------- Dados do servidor ---------------------#
servidor = "127.0.0.1"
porta = 43210
#---------------------- Condfigura��o do cliente ---------------------#
obj_socket = socket(AF_INET,SOCK_DGRAM) #cria aplica��o UDP
obj_socket.connect((servidor,porta)) #executa como cliente
saida = ""
#---------------------- Intera��o com o servidor ---------------------#
while saida != "X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(),(servidor,porta)) # envia msg(bytes) para o servidor
    dados,origem = obj_socket.recvfrom(65535) #recebe msg(bytes) do servidor
    print("Resposta do sevidor: ",dados.decode()) #exibe msg(string) do servidor
    saida = input("Digite <X> para sair: ").upper() #entrada de dados do while
obj_socket.close() #fecha conex�o