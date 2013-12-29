#!/usr/bin/pytho
import serial
import mosquitto
import os
import time
import calendar
import json
import ConfigParser

serialdev = '/dev/ttyO1'
broker = "127.0.0.1"
port = 1883
 
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

def on_connect(rc):
	if rc == 0:
		#rc 0 successful connect
		print "433mhz -> MQTT Connected"
	else:
		raise Exception
 
 
def on_publish(val):
	print "Published 433mhz ", val
 
def cleanup():
	print "Ending and cleaning up"
	ser.close()
	mqttc.disconnect()
 
def main():
	try:
		print "Connecting... ", serialdev
		#connec	 to serial port
		ser = serial.Serial(serialdev, 9600, timeout=20)
	except:
		print "Failed to connect serial"
		#unable to continue with no serial input
		raise SystemExit
 
 
	try:
		ser.flushInput()
		mypid = os.getpid()
		client_uniq = "arduino_pub_"+str(mypid)
		mqttc = mosquitto.Mosquitto(client_uniq)
 	
		mqttc.on_connect = on_connect
		mqttc.on_publish = on_publish
		mqttc.connect(broker, port, 60, True)

		lastline = None
		lastpublish = 0

		while mqttc.loop() == 0:
			line = ser.readline()
			gap = calendar.timegm(time.gmtime()) - lastpublish
			try:
		                data = json.loads(line)
				print data
                		try:
					device_id[data['DEVICE'][0]['D']]()
        	        		if data['DEVICE'][0]['D'] == 11:
						result = hex(int(data['DEVICE'][0]['DA'],2))
						json_data = json.dumps(["433mhz", result]) 
						if gap < 10:
							if line == lastline:
								pass
							else:
								mqttc.publish("sensors", json_data)
								lastpublish =  calendar.timegm(time.gmtime())
						else:
							mqttc.publish("sensors", json_data)
							lastpublish =  calendar.timegm(time.gmtime())
						lastline = line
					else:
						print "Other sensors - not implemented"
				except KeyError:
					pass
	        	except ValueError:
        	        	print "Invalid JSON"


			pass 
 
	except (IndexError):
		print "No data received within serial timeout period"
		cleanup()
	except (KeyboardInterrupt):
		print "Interrupt received"
		cleanup()
	except (RuntimeError):
		print "uh-oh! time to die"
		cleanup()
