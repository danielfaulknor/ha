#!/usr/bin/python

import mosquitto
import json
import time

def switch(dev, intent, data = None):
	print dev
	if intent == "on":
		print  "switch_"+ dev +"_on"
		mqttc.publish("433mhz/send", "switch_"+ str(dev) +"_on" )
	if intent == "off":
		mqttc.publish("433mhz/send", "switch_"+ str(dev) +"_off" )

def on_connect(rc):
	print "ACTUARTORS Connected to MQTT"

#runs when a MQTT message arrives
def on_message(msg):
	#unpack json payload
	inbound = json.loads(msg.payload)
	
	#this is the device we are working with...
	cat = inbound[0]
	dev = inbound[1]
	#....and what we want to do with it
	intent = inbound[2]
	#some things need extra info
	data = None
	try:
		data = inbound[3]
	except IndexError:
		pass
	#use the lookup table to run the command for the device
	actuator[cat](dev, intent, data)

def main():

	try:	
		actuator = {
        		"switch" : switch,
		}


		print "actuators"
		#start up the MQTT connection
		mqttc = mosquitto.Mosquitto("actuators")
		mqttc.on_message = on_message
		mqttc.on_connect = on_connect
		mqttc.connect("127.0.0.1", 1883, 60, False)
		mqttc.subscribe("actuators", 0)

		#infinite loop until the MQTT connection dies
		while mqttc.loop() == 0:
			pass
	except KeyboardInterrupt:
		pass
