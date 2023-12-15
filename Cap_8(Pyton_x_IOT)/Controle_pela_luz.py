
import serial
from serial.tools import list_ports

#lista as portas do arduino
conexao = ""
for por in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(por.description, port.device))
    if("ARDUINO" in por.description.upper()):
        try:
            conexao = serial.Serial(port.device,115200)
            print("Conexao realizada com {}.".format(conexao.portstr))
        except:
            pass
if conexao != "":
    print("Iniciando...")
    while True:
        print("Recebendo dados...")
        resposta = conexao.readline()
        valor = float(resposta.decode())
        print(valor)
        if(valor<700):
            conexao.write(b'1')
        else:
            print("Sem portas disponiveis")