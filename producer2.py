'''
Created on Apr 21, 2017

@author: jackwang
'''
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
from datetime import datetime


log = logging.getLogger()

producer = KafkaProducer(bootstrap_servers='34.201.178.24:9092')

# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')

# produce asynchronously
for i in range(100):
    date_object = datetime.now()
    current_time = date_object.strftime('%H:%M:%S')
    producer.send('my-topic', key=b'iteration', value="Message Time Stamped #" + str(i))

# block until all async messages are sent
producer.flush()
producer.close()

