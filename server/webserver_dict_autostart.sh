#!/bin/bash

echo "entering virtual environment..."
cd /home/pi/photobooth/.venv
source bin/activate
cd ~

echo "removing DS Files"
cd /home/pi/photobooth/server/static/Images
find . -name '.DS_Store' -type f -delete

echo "starting webserver..."
cd /home/pi/photobooth/server
export FLASK_APP=webserver_dict.py
flask run -h 192.168.1.2

$SHELL
