import pika

from .hello_handler import hello_handler

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    result = channel.queue_declare(queue='', exclusive=True)
    channel.queue_bind(exchange='hello', queue=result.method.queue)
    channel.basic_consume(queue=result.method.queue, auto_ack=True, on_message_callback=hello_handler)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
