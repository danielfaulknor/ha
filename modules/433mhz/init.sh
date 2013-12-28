#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$DIR/mqtt_2_433mhz.py &
$DIR/433mhz_2_mqtt.py &
