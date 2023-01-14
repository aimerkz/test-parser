#!/bin/bash

NAME="test-parser"

echo "Starting" $NAME
sleep 2

echo "Creating and activating a virtual environment"
sleep 2

python3 -m ./venv venv
source ./venv/bin/activate

echo "Installing dependencies"
sleep 2

pip3 install -r requirements.txt

echo "Running"
sleep 2

python3 main.py
