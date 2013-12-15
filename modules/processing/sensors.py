#!/usr/bin/python

import mosquitto
import json

def sensor_LaundryDoor():
	print "Laundry Door Opened"
	mqttc.publish("actuators", json.dumps(["switch_HallLight", "on"]))
rf_433mhz = { 
	"0x471d5c" : sensor_LaundryDoor,	
}

def on_connect(rc):
	print "Connected to MQTT"

def on_message(msg):
	inbound = json.loads(msg.payload)
	medium = inbound[0]
	content = inbound[1]

	if str(medium) == "433mhz":
		try:
			rf_433mhz[str(content)]()
		except:
			print "Sorry code " + content + " is not setup"
	else:
		print "Medium " + medium + " not implemented!"

mqttc = mosquitto.Mosquitto("sensors")

mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect("127.0.0.1", 1883, 60, False)

mqttc.subscribe("sensors", 0)

while mqttc.loop() == 0:
	pass

