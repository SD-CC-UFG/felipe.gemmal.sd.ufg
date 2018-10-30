#Servidor intermediario para acesso indireto de Felipe Gemmal
# -*- coding: utf-8 -*-
import socket
import sys
import threading


names = {"1":"12391", "2":"12392", "3":"12393"}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
porta = 12345



def cliente(connection,porta):

	print("Thread criada")
	nomeServico= str(connection.recv(1024).decode('utf-8'))
		
	if nomeServico == "":
		print("Sem dados")
		return

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
	print(nomeServico)
	endereco = names.get(nomeServico,-1)
	
	if(endereco == -1):
		print("Nome nao existe")
	
	else:
		connection.send("localhost"+" "+ endereco)
		
	#conexao.close()
	connection.close()	
	return


def newService(connection,cliente):
	print("Thread criada")
	novoServico= str(connection.recv(1024).decode('utf-8')).split(" ")
	

	#print("Colocando a chave: "+novoServico[0]+" e valor : "+novoServico[1]+" no dicionario")

	#print("Tamanho da lista de strings "+ str(len(novoServico)) )
	#print("Service String:"+novoServico[0])


	names.update({novoServico[0] : novoServico[1]})

	print("Novo servico adicionado: "+novoServico[0]+" "+names.get(novoServico[0]) )
	
	return



server.bind((ip,porta))
server.listen(10)

print("Esperando conexao")
while True:
	
	co,endCliente = server.accept()
	print("Conexao aceita")

	tipo= str(co.recv(1024).decode('utf-8'))

	print(tipo +' Criando thread')
	if(tipo == 'request'):
		linha = threading.Thread(target=cliente,args=(co,porta))
		linha.start()

	elif(tipo == 'addservice'):
		linha = threading.Thread(target=newService,args=(co,endCliente))
		linha.start()
	

server.close()


