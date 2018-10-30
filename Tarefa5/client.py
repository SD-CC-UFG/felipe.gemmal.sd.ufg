#Cliente basico acesso indireto de Felipe Gemmal
# -*- coding: utf-8 -*-
import os
import socket, string
import sys

nameServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
porta = 12345

nameServer.connect((ip,porta))



while True:
	#tipo de servico requisitado, colocado aqui por conta do tempo de recv do dns
	nameServer.send("addservice")

	print("Se quiser salario- 1 + salario")
	print("Se quiser maior idade - 2 + sexo(F/M) + idade (lista 2)")
	print("Se quiser peso ideal - 3 + altura + sexo(F/M) ( lista 4)")

	opcao = raw_input()

	#if int(opcao) == 1:
	#	dados = raw_input()

	#elif int(opcao) == 2:
	#	sexo = raw_input()
	#	idade = raw_input()
	#	dados = sexo +" "+idade
	#else:
	#	altura = raw_input()
	#	sexo = raw_input()
	#	dados = altura+" "+sexo



	print("Buscando endereco do servico")
	
	nameServer.send(opcao)

	os.system('clear')
	
	print("Esperando resposta:")
	mensagem = str(nameServer.recv(1024).decode('utf-8')).split()

	print(mensagem)


	print("Conectando no servidor de servico:")
	servico.connect((mensagem[0],int(mensagem[1]) ))


	print("Enviando dados")
	servico.send(dados)

	resposta = str(servico.recv(1024).decode('utf-8')).split()
	print("Resposta:")
	print(resposta[0])
	
	servico.close()

nameServer.close()