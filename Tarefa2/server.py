#Servidor para cliente Multi-thread de Felipe Gemmal
import socket
import sys
import threading


def cliente(connection,client,nome):
	print ("Novo membro conectado")
	
	while True:
		
		recv = connection.recv(1024).decode('utf-8')
		if(recv == ''):
			print("%s Desconectou"%nome)
			break
		print ("%s: %s" %(nome,recv))
		
		#print ("Thread%d disse: %s" % (threading.get_ident(),recv))
		

	connection.close()
	#self._Thread_stop()	



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12345

server.bind((ip,porta))
server.listen(10)

print("Esperando conexao")
while True:
	co,pedido = server.accept()
	nome= co.recv(1024).decode('utf-8')
	linha = threading.Thread(target=cliente,args=(co,pedido,nome))
	linha.start()


