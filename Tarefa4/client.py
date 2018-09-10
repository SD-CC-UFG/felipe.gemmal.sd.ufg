#Cliente basico acesso indireto de Felipe Gemmal

import socket, string
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
porta = 12349

server.connect((ip,porta))

while True:
	opcao = raw_input()
	dados = raw_input()
	
	if(opcao == 'batata'):
		break
	server.send(opcao+" "+dados)

	print("Esperando resposta:")
	mensagem = server.recv(1024)
	print("Resposta:")
	print(mensagem)

server.close()