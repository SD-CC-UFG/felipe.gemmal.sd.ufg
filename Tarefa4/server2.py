#Servidor para cliente de acesso indireto de Felipe Gemmal
import socket
import sys
import threading


def cliente(connection,client):
	pedido= str(connection.recv(1024).decode('utf-8')).split()
		
	if pedido[0] == "F":
		if int(pedido[1]) >= 21:
			print("Entrei 1")
			resposta = "Sim"
		else:
			print("Entrei 2")
			resposta = "Nao"

	elif pedido[0] == "M":
		if int(pedido[1]) >= 18:
			print("Entrei 3")
			resposta = "Sim"
		else:
			print("Entrei 4")
			resposta = "Nao"
	else:
		print("Entrei 5")
		resposta = "Nao"
	
	connection.send(resposta)
		
	connection.close()	


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12343 + 2

server.bind((ip,porta))
server.listen(10)

print("Servidor 2 ativo")
print("Esperando pedidos do DNS")
while True:
	co,pedido = server.accept()
	linha = threading.Thread(target=cliente,args=(co,pedido))
	linha.start()

server.close()
