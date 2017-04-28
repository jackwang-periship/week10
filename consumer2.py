'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaConsumer
import logging


log = logging.getLogger()

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic',
                         bootstrap_servers=['34.201.178.24:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

