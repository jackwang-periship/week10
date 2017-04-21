'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaClient, SimpleProducer, SimpleConsumer


kafka = KafkaClient("localhost:9092")
consumer = SimpleConsumer(kafka, "python", "first")
for msg in consumer:
    print msg
