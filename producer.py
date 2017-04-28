'''
Created on Apr 21, 2017

@author: jackwang
'''

from kafka import KafkaProducer
from datetime import datetime


producer = KafkaProducer(bootstrap_servers='34.201.178.24:9092')
producer.send("pythontest", "This is message sent from python client " + str(datetime.now().time()) )

print "Done!"