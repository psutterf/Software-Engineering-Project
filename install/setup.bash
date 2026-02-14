#!/bin/bash
 
set -e  

sudo -v  #prompts user password

sudo apt update

echo
echo "=====DOWNLOADING PYTHON DEPENDANCIES=====" 
echo 

sudo apt install -y python3-pip python3-tk

pip install --user psycopg2-binary  #will have to update this line if adding more libraries can use a -r requirements.txt file in the future 

echo "setup complete"