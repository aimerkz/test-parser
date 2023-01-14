#!/bin/bash

NAME="test-parser"
DJANGODIR=test-parser/

echo "Starting" $NAME
sleep 2

cd $DJANGODIR

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
