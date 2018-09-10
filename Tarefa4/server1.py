#Servidor para cliente de acesso indireto de Felipe Gemmal
import socket
import sys
import threading


def cliente(connection,client):
	pedido= str(connection.recv(1024).decode('utf-8')).split()
		
	resposta = int(pedido[0]) * 10
	connection.send(str(resposta))
		

	connection.close()	




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12349 + 1

server.bind((ip,porta))
server.listen(10)

print("Servidor 1 ativo")
print("Esperando pedidos do DNS")
while True:
	co,pedido = server.accept()
	linha = threading.Thread(target=cliente,args=(co,pedido))
	linha.start()


