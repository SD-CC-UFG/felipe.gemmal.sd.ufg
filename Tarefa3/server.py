import pika
import sys
import datetime
import threading


connectionSubscribe = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel_to_subscribe = connectionSubscribe.channel()

channel_to_subscribe.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel_to_subscribe.queue_declare(durable = True)
queue_name = result.method.queue

channel_to_subscribe.queue_bind(exchange='direct_logs', queue=queue_name, routing_key = 'cliente')


def callback(ch, method, properties, body):
	
	connectionPublish = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel_to_publish = connectionPublish.channel()

	channel_to_publish.exchange_declare(exchange='direct_logs', exchange_type='direct')

	mensagem = body

	print mensagem

	channel_to_publish.basic_publish(exchange='direct_logs', routing_key='servidor', body=mensagem, properties=pika.BasicProperties(
		delivery_mode = 2, # make message persistent
    ))

	connectionPublish.close()


channel_to_subscribe.basic_consume(callback, queue=queue_name, no_ack=True)

def consome():
	channel_to_subscribe.start_consuming()

t1 = threading.Thread(target=consome, args=[])
t1.start()


