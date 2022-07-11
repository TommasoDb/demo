#!/usr/bin/env bash

set -e

function create_venv() {
    VENV_DIR="$1"
    echo "Creating virtualenv for Python in '$VENV_DIR'"
    python -m venv ${VENV_DIR}
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    deactivate
}

create_venv venv

