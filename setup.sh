#!/bin/bash

# Export SECRET_KEY
echo "Setup Secret Key:START"
if ! grep -wq FLASK_SECRET_KEY ~/.bashrc
then
  echo "FLASK_SECRET_KEY=$(hexdump -vn "64" -e ' /1 "%02x"'  /dev/urandom)" >> ~/.bashrc
  echo "Exporting Secret Key"
fi
source ~/.bashrc
echo "Setup Secret Key:COMPLETED"

# Setup Python Environment
echo "Setup Pipenv"
sudo apt install pipenv -y
echo "Deploy from Pipfile:START"
pipenv --three
pipenv install --system
echo "Deploy from Pipfile:COMPLETED"