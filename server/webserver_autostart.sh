#!/bin/bash

echo "entering virtual environment..."
cd /home/pi/Documents/photobooth/.venv
source bin/activate
cd ~

echo "removing DS Files"
cd /home/pi/Documents/photobooth/server/static/Images
find . -name '.DS_Store' -type f -delete

echo "starting webserver..."
cd /home/pi/Documents/photobooth/server
export FLASK_APP=webserver.py
flask run -h 192.168.0.18

$SHELL
