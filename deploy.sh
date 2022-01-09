#!/bin/bash

MAXWELL_HOME="/opt/fdc/maxwell"
MAXWELL_DATA_PROCESSOR_HOME="$MAXWELL_HOME/data-processor"
pushd "$MAXWELL_DATA_PROCESSOR_HOME"
sudo systemctl stop maxwell-data-processor
git pull origin $MAXWELL_DATA_PROCESSOR_GIT_BRANCH
source venv/bin/activate
pip install -r requirements.txt
deactivate
sudo systemctl daemon-reload
sudo systemctl start maxwell-data-processor
popd
