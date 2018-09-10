#Servidor intermediario para acesso indireto de Felipe Gemmal

import socket
import sys
import threading


def cliente(connection,client,porta):

	while True:
		direcao= str(connection.recv(1024).decode('utf-8')).split()

		conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		entrada = int(direcao[0]) + porta
		conexao.connect(("localhost",entrada))

		print("O valor da entrada eh:")
		print(entrada)
	
		conexao.send(direcao[1])
		resposta = conexao.recv(1024)

		connection.send(resposta)
		
		conexao.close()
	connection.close()	




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12349

server.bind((ip,porta))
server.listen(10)

print("Esperando conexao")
while True:
	co,pedido = server.accept()
	linha = threading.Thread(target=cliente,args=(co,pedido,porta))
	linha.start()


