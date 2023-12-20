from confluent_kafka import Producer
import json
import socket

topic = 'topic_user_created'
class producerUserCreated:
    def __init__(self) -> None:
        conf = {
            'bootsrap.servers': "localhost:9092",
            'client.id': socket.gethostbyname()}
        self.producer = Producer

    def publish(self, method, body):
        print('Inside main: Sending to kafka')
        print(body)
        self.producer.produce(topic, key='key.user.created', value=json.dumps(body))