import time
import json
import paho.mqtt.client as paho

broker="10.20.1.95"

def on_message(client, userdata, message):
    time.sleep(1)
    jsonMessage = json.loads(message.payload)
    publishedMessage = "{\nStudentID: " + str(jsonMessage["StudentID"]) + "\nName: " + str(jsonMessage["Name"]) + "\nSurname: " + str(jsonMessage["Surname"]) + "\nTelephone: " + str(jsonMessage["Telephone"]) + "\nGrade: " + str(jsonMessage["Grade"])+"\n }"
    print("received JSON =\n", publishedMessage)

client= paho.Client() 

client.on_message=on_message


print("connecting to broker ",broker)
client.connect(broker)
client.loop_start() 
print("subscribing...")
client.subscribe("se443/midterm2")
while(True):
	client.on_message=on_message