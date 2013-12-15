#!/usr/bin/python

import mosquitto
import json
import time

def switch_HallLight(intent, data = None):
	if intent == "on":
		time.sleep(1)
		mqttc.publish("433mhz/send", "switch_HallLight_on")
	if intent == "off":
		print "Turning to the off"

actuator = {
        "switch_HallLight" : switch_HallLight,
}

def on_connect(rc):
	print "Connected to MQTT"

def on_message(msg):
	inbound = json.loads(msg.payload)
	dev = inbound[0]
	intent = inbound[1]
	data = None
	try:
		data = inbound[2]
	except IndexError:
		pass
	actuator[dev](intent, data)



mqttc = mosquitto.Mosquitto("actuators")

mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect("127.0.0.1", 1883, 60, False)

mqttc.subscribe("actuators", 0)

while mqttc.loop() == 0:
	pass

