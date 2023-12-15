
from socket import * #Este tipo de import pega todos os metodos da biblioteca
#---------------------- Configuração do servidor ----------------------#
servidor = "127.0.0.1" # define o endereço(id) do servidor(localhost)
porta = 43210 # define a porta de entrada

obj_socket = socket(AF_INET,SOCK_STREAM) # cria aplicação TCP
# AF_INET:tipo de id,SOCK_STREAM:tipo de potocolo

obj_socket.bind((servidor,porta)) #executa como aplicação servidora
obj_socket.listen(2) # define o numero maximo de clientes q podem conectar

#---------------------- Interação com o cliente ----------------------#
print("Aguardando CLiente....") #informa que server ta em execução
while True: # aguarda por clientes
    con, cliente = obj_socket.accept() # metodo que confirma conexão
    # quando o cliente se conecta, é informado tipo de conexão e o identificador do cliente(tupla)
    print("Conectado com: ",cliente)
    while True: # aguarda a ação do cliente
        msg_recebida = str(con.recv(1024)) #espera uma mensagem(pacote) do cliente para confirmar conexão
        # recv(maximo de bytes do pacote)
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente' #'b'pra dizer q ta em bytes
        con.send(msg_enviada) # Envia uma mensagem pro cliente
        break #fecha o laço de informações
    con.close() #fecha conexão e aguarda por outros clientes.