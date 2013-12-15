#!/usr/bin/python

import mosquitto
import json

def rfm():
    print "433mhz"

def humidity():
    print "H"

def temperature():
    print "T"

def undef():
    print "Ignore"

device_id = {11 : rfm,
                30 : humidity,
                31 : temperature,
		999 : undef,
		1007 : undef,
}

def on_connect(rc):
	print "Connected"

def on_message(msg):
	try:
		print msg.payload
		data = json.loads(msg.payload)
		device_id[data['DEVICE'][0]['D']]()
		if data['DEVICE'][0]['D'] == 11:
			print hex(int(data['DEVICE'][0]['DA'],2))
		else:
			print data['DEVICE'][0]['DA']
	except ValueError:
		print "Invalid JSON"

mqttc = mosquitto.Mosquitto("decode_433mhz")

mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect("127.0.0.1", 1883, 60, False)

mqttc.subscribe("433mhz/recieve", 2)

while mqttc.loop() == 0:
	pass

