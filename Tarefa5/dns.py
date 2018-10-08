#Servidor intermediario para acesso indireto de Felipe Gemmal
# -*- coding: utf-8 -*-
import socket
import sys
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12344



def cliente(connection,client,porta):

	while True:
		direcao= str(connection.recv(1024).decode('utf-8'))
		
		if direcao == "":
			continue

		#conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#entrada = int(direcao[0]) + porta
		
		#if int(direcao[0]) == 1:
		#	dados = direcao[1]

		#elif int(direcao[0]) == 2:
		#	sexo = direcao[1]
		#	idade = direcao[2]
		#	dados = sexo +" "+idade
		#else:
		#	altura = direcao[1]
		#	sexo = direcao[2]
		#	dados = altura+" "+sexo


		#conexao.connect(("localhost",entrada))

		#print("O valor da entrada eh:")
		#print(entrada)
	
		#conexao.send(dados)
		#resposta = conexao.recv(1024)

		#resposta = "localhost"+" "+direcao[0]
		print(direcao)
		direcao = str(int(direcao) + porta)
		

		connection.send("localhost"+" "+ direcao)
		
		#conexao.close()
	connection.close()	




server.bind((ip,porta))
server.listen(10)

print("Esperando conexao")
while True:
	co,pedido = server.accept()
	linha = threading.Thread(target=cliente,args=(co,pedido,porta))
	linha.start()

server.close()


