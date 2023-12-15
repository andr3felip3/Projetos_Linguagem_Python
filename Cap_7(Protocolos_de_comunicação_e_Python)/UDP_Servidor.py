from socket import *
#---------------------- Configuração do servidor -------------------#
servidor = "127.0.0.1"
porta = 43210
obj_socket = socket(AF_INET,SOCK_DGRAM) #Cria aplicação UDP
obj_socket.bind((servidor,porta)) #executa como servidor
print("Servidor Pronto")
#---------------------- Interação com o cliente ---------------------#
while True:
    dados, origem = obj_socket.recvfrom(65535)
    # recvfrom(n):define n maquinas que podem conectar(max:65535)
    print("Origem.......:", origem) #id do cliente conectado
    print("Dados recebidos.: ",dados.decode()) #mensagem recebida do cliente
    # decode():decodifica uma msg de bytes p/ string
    resposta = input("Digite a resposta: ") #mensagem para ser enviada ao clinete
    obj_socket.sendto(resposta.encode(), origem) #envia msg codificada para o cliente
    # sendto(msg,idcliente): envia msg para o cliente
    # encode(): codifica a msg de string para bytes.
obj_socket.close() #fecha conexão