#!/bin/bash

echo "===== LazerTag System Check ====="
echo

echo "Python version:"
python3 --version

echo
echo "Pip version:"
python3 -m pip --version

echo
echo "Tkinter version:"
python3 -c "import tkinter; print('tkinter installed')"

echo
echo "psycopg2 version:"
python3 -c "import psycopg2; print(psycopg2.__version__)"


echo "system is ready for use"