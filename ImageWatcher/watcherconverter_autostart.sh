#!/bin/bash

echo "starting image converter..."
cd /home/pi/photobooth/ImageWatcher
python3 ImageConverter.py

echo "starting image watcher..."
python3 ImageWatcher.py

echo "running"

$SHELL
