#Trabalhando com arduino 

import serial
from serial.tools import list_ports
#lista de portas do arduino
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))

conexao = serial.Serial('COM3',115200)

acao = input("Digite:\n<L> para ligar\n<D> para desligar: ").upper()
while acao == "L" or acao == "D":
    if acao == "L":
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    acao = input("Digite: \n<L> para ligar\n<D> para desligar: ").upper()
conexao.close()
print("Conexao encerrada")