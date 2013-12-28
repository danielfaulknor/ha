#!/bin/bash
APP_PATH=/root/ha
find $APP_PATH/modules -name "init.sh" -exec bash {} \;
bash
