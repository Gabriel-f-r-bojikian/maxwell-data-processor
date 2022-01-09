#!/bin/bash

MAXWELL_HOME="/opt/fdc/maxwell"
MAXWELL_DATA_PROCESSOR_HOME="$MAXWELL_HOME/data-processor"

install_python_packages() {
    if [ -e "$MAXWELL_DATA_PROCESSOR_HOME/requirements.txt" ]; then
        echo "Installing additional Python packages"
        pip install -r "$MAXWELL_DATA_PROCESSOR_HOME/requirements.txt"
    fi
}

## Install Packages
python3 -m venv venv
source "$MAXWELL_DATA_PROCESSOR_HOME/venv/bin/activate"
python -m pip install --upgrade pip
pip install --upgrade cython
pip install wheel

# Install requirements
install_python_packages
