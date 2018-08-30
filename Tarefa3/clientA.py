import pika
import sys
import datetime
import threading

global user

connectionSubscribe = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel_to_subscribe = connectionSubscribe.channel()

channel_to_subscribe.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel_to_subscribe.queue_declare(durable = True)
queue_name = result.method.queue

channel_to_subscribe.queue_bind(exchange='direct_logs', queue=queue_name, routing_key = 'servidor')

def consome():
	channel_to_subscribe.basic_consume(callback, queue=queue_name, no_ack=True)
	channel_to_subscribe.start_consuming()

def attChat( mensagem ):
	info = str(mensagem).split()
	
	if(info[0].find(user) == -1):
		print (mensagem)

def callback(ch, method, properties, body):	
	attChat(str(body))


def publicaChat (mensagem):
	connectionPublish = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel_to_publish = connectionPublish.channel()

	channel_to_publish.exchange_declare(exchange='direct_logs', exchange_type='direct')

	mensagem = user + ": " + mensagem

	channel_to_publish.basic_publish(exchange='direct_logs', routing_key='cliente', body=mensagem, properties=pika.BasicProperties(
		delivery_mode = 2, # make message persistent
    ))

	connectionPublish.close()

def escreve ():
	while( True ):
		readAll = raw_input()
		publicaChat(readAll)

print("Digite o seu nome: ")

user= raw_input()

t1 = threading.Thread(target=consome, args=[])
t2 = threading.Thread(target=escreve, args=[])

t1.start()
t2.start()