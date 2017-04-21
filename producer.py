'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaClient, SimpleProducer, SimpleConsumer


kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
producer.send_messages("first", "hello python!")
producer.send_messages("first", "hello again!", "nice to meet you")
producer = SimpleProducer(kafka, async=True)
