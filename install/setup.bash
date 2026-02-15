set -e

sudo -v   # Prompt for password once

sudo apt update

echo
echo "===== DOWNLOADING PYTHON DEPENDENCIES ====="
echo

sudo apt install -y \
    python3-pip \
    python3-tk \
    python3-psycopg2 \
    python3-pil \
    python3-pil.imagetk

echo
echo "===== SETUP COMPLETE ====="