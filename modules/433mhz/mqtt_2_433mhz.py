#!/usr/bin/python

import mosquitto
import serial
from codes import s_433mhz

def hextobin(hexval):
        thelen = len(hexval)*4
        binval = bin(int(hexval, 16))[2:]
        while ((len(binval)) < thelen):
            binval = '0' + binval
        return binval

def on_connect(rc):
	print "Connected 433mhz -> MQTT"

def on_message(msg):
	print "Payload: " + msg.payload
	payload = s_433mhz[msg.payload]
	print "Sending " + payload
	ser = serial.Serial("/dev/ttyO1", 9600)  #open serial port
	print '{"DEVICE":[{"G":"0","V":0,"D":11,"DA":"' + hextobin(payload) + '"}]}'
	ser.write('{"DEVICE":[{"G":"0","V":0,"D":11,"DA":"' + hextobin(payload) + '"}]}')
	ser.close()

mqttc = mosquitto.Mosquitto("2_433mhz")

mqttc.on_message = on_message
mqttc.on_connect = on_connect

mqttc.connect("127.0.0.1", 1883, 60, True)

mqttc.subscribe("433mhz/send", 2)

while mqttc.loop() == 0:
	pass

