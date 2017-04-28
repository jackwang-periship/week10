'''
Created on Apr 21, 2017

@author: jackwang
'''

from kafka import KafkaConsumer


consumer = KafkaConsumer(bootstrap_servers='34.201.178.24:9092',
                                 auto_offset_reset='earliest')
consumer.subscribe(['pythontest'])
for message in consumer:
    print (message)

print "Done!"
