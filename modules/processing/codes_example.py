def sensor_SomeDoor():
        print "Some Door Opened"
        mqttc.publish("actuators", json.dumps(["switch_HallLight", "on"]))

rf_433mhz = {
        "0x471d1e" : sensor_SomeDoor,
}
