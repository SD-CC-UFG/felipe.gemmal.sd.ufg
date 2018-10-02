#Cliente basico acesso indireto de Felipe Gemmal

import socket, string
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
porta = 12343

server.connect((ip,porta))

#socket que ira conectar no serviço
#servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
	print("Se quiser salario- 1 + salario")
	print("Se quiser maior idade - 2 + sexo(F/M) + idade (lista 2)")
	print("Se quiser peso ideal - 3 + altura + sexo(F/M) ( lista 4)")

	opcao = raw_input()

	if int(opcao) == 1:
		dados = raw_input()

	elif int(opcao) == 2:
		sexo = raw_input()
		idade = raw_input()
		dados = sexo +" "+idade
	else:
		altura = raw_input()
		sexo = raw_input()
		dados = altura+" "+sexo

	server.send(opcao+" "+dados)

	# enviar apenas qual o serviço desejado para o serviço de nomes
	#server.send(opcao)
	print("Esperando resposta:")
	mensagem = server.recv(1024)

	#conectar o socket nesse serviço
	#mensagem = str(server.recv(1024).decode('utf-8')).split())
	#servico.connect((mensagem[0],mensagem[1]))

	#resposta =servico.send(dados)

	print("Resposta:")
	print(mensagem)

	#mostrar na tela a resposta
	#print(resposta)

server.close()