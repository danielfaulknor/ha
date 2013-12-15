#!/bin/bash
APP_PATH=/root/ha
$APP_PATH/modules/433mhz/mqtt_2_433mhz.py &
$APP_PATH/modules/433mhz/433mhz_2_mqtt.py &
bash
