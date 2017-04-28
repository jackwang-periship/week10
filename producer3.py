'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaProducer
import msgpack
import logging


log = logging.getLogger()

# produce msgpack messages
producer = KafkaProducer(bootstrap_servers='34.201.178.24:9092',
                         value_serializer=msgpack.dumps)
producer.send('msgpack-topic', {'key': 'value'})

# block until all async messages are sent
producer.flush()

print "Done!"
