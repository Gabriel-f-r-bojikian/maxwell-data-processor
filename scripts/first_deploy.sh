#!/bin/bash

# First time
MAXWELL_HOME="/opt/fdc/maxwell"
MAXWELL_DATA_PROCESSOR_HOME="$MAXWELL_HOME/data-processor"
pushd $MAXWELL_HOME
git config --global user.name "Henrique Spadim"
git config --global user.email "henrique@spadim.com.br"
git config --global credential.helper cache
git clone -b $MAXWELL_DATA_PROCESSOR_GIT_BRANCH --single-branch https://github.com/Gabriel-f-r-bojikian/maxwell-data-processor data-processor
pushd "$MAXWELL_DATA_PROCESSOR_HOME"
git checkout $MAXWELL_DATA_PROCESSOR_GIT_BRANCH
source "$MAXWELL_DATA_PROCESSOR_HOME/scripts/installation.sh"
sudo systemctl enable "$MAXWELL_DATA_PROCESSOR_HOME/services/maxwell-data-processor.service"
sudo systemctl daemon-reload
sudo systemctl start maxwell-data-processor
popd
popd