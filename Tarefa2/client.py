#Cliente basico em chat Multi-thread de Felipe Gemmal

import socket, string
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
porta = 12345

server.connect((ip,porta))
print("Conectado! Para sair digite batata")
print ("Digite seu nome")
nome = raw_input()
server.send(nome.encode('utf-8'))

while True:
	envio = raw_input()
	
	if(envio == 'batata'):
		break

	server.send(envio.encode('utf-8'))
	print("Mensagem enviada!")


server.close()