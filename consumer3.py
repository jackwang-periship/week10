'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import msgpack
import json
import logging


log = logging.getLogger()

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         value_deserializer=msgpack.unpackb,
                         bootstrap_servers=['34.201.178.24:9092'])
consumer.subscribe(['msgpack-topic'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

    
print "Done!"

