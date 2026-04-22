#!/bin/bash
set -e

sudo -v

echo
echo "===== INSTALLING SYSTEM DEPENDENCIES ====="
echo

sudo apt update

sudo apt install -y \
    python3 \
    python3-pip \
    python3-tk \
    python3-pil \
    python3-pil.imagetk \
    python3-psycopg2 \
    python3-pygame

echo
echo "===== SETUP COMPLETE ====="
echo