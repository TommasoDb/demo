#!/usr/bin/env bash
chmod +x install.sh
./install.sh
source venv/bin/activate
python -m pytest -s tests.py

deactivate
