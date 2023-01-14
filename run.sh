#!/bin/bash

NAME="test-parser"
FILE="parser/static/data.json"
TIME=2

echo "Starting" $NAME
sleep $TIME

echo "Creating and activating a virtual environment"
sleep $TIME

python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies"
sleep $TIME

pip3 install -r requirements.txt

echo "Running"
sleep $TIME

echo "Input data"
echo " $(cat $FILE)"

echo "Output data"
sleep $TIME

python3 main.py
sleep $TIME

echo "Done"
