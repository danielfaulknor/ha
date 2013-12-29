#!/usr/bin/python

import mosquitto
import json
import time
import codes

def on_connect(rc):
	print "SENSORS Connected to MQTT"

def on_message(msg):
	inbound = json.loads(msg.payload)
	medium = inbound[0]
	content = inbound[1]

	if str(medium) == "433mhz":
		try:
			codes.rf_433mhz[str(content)]()
		except:
			print "Sorry code " + content + " is not setup"
	else:
		print "Medium " + medium + " not implemented!"


def main():

	try:
		mqttc = mosquitto.Mosquitto("sensors")

		mqttc.on_message = on_message
		mqttc.on_connect = on_connect
	
		mqttc.connect("127.0.0.1", 1883, 60, False)

		mqttc.subscribe("sensors", 0)

		while mqttc.loop() == 0:
			pass
	except KeyboardInterrupt:
		pass
