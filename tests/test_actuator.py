#!/usr/bin/python
import mosquitto
import os
import json
import time

serialdev = '/dev/ttyO1'
broker = "127.0.0.1"
port = 1883
 
def on_connect(rc):
        print "Connected"

def on_connect(rc):
	if rc == 0:
		#rc 0 successful connect
		print "Actuator test connected to MQTT"
	else:
		raise Exception
 
 
def on_publish(val):
	print "Published ", val
 
def cleanup():
	print "Ending and cleaning up"
	ser.close()
	mqttc.disconnect()
 
mypid = os.getpid()
client_uniq = "arduino_pub_"+str(mypid)
mqttc = mosquitto.Mosquitto(client_uniq)

mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.connect(broker, port, 60, True)

while mqttc.loop() == 0:
	mqttc.publish("actuators", json.dumps(["switch", "WalkwayLight", "on"]))
	time.sleep(0.5)
	mqttc.publish("actuators", json.dumps(["switch", "WalkwayLight", "off"]))	
	time.sleep(0.5)
	mqttc.publish("actuators", json.dumps(["switch", "WalkwayLight", "on"]))
	time.sleep(0.5)
	mqttc.publish("actuators", json.dumps(["switch", "WalkwayLight", "off"]))	
	time.sleep(0.5)

	break
	pass 
