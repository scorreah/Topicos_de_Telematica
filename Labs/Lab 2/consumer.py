import pika
import json
import config
import time
import ubidots_request

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(config.MOM_IP, config.MOM_PORT, '/',
    pika.PlainCredentials(config.MOM_USERNAME, config.MOM_PASSWD)))

    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f'{json.loads(body)} is received')
        ubidots_request.post_request(json.loads(body))
        
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    while(True):
        main()
        time.sleep(4)