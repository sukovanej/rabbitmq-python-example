import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.basic_publish(exchange='hello', routing_key='', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
