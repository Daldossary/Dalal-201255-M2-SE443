import paho.mqtt.client as mqtt
import json

broker_address="10.20.1.95"

client = mqtt.Client()

topic = "se443/midterm2"

#TYPE OUT UR JSON IN THIS SYNTAX
message =  '{ "StudentID":201255, "Name":"Dalal", "Surname":"Aldossary", "Telephone":"0537578888", "Grade":4}'

if (client.connect(broker_address,1883,60) ==0):
	print ("Connected successfully to "+broker_address)
	
client.publish(topic, message)
print ("Published in "+topic+", JSON = \n"+message)
client.disconnect();