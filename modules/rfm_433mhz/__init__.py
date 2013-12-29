#!/usr/bin/python

import input_to_mqtt

def main():
	try:
		input_to_mqtt.main()
	except KeyboardInterrupt:
		pass 	
	#output_to_433mhz.main()
