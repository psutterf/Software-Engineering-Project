#!/bin/bash
set -e

sudo -v   # prompt for password once

sudo apt update

echo
echo "===== INSTALLING SYSTEM DEPENDENCIES ====="
echo

sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-tk

python3 -m venv venv    # creates python virtual enviornment

source venv/bin/activate

echo
echo "===== INSTALLING PYTHON LIBRARIES ====="
echo

pip install --upgrade pip
pip install -r requirements.txt

echo
echo "===== SETUP COMPLETE ====="
echo