#!/usr/bin/env bash
set -e

set -a
source "/opt/conf/maxwell-data-processor.conf"
set +a

pushd $MAXWELL_DATA_PROCESSOR_HOME
source venv/bin/activate
python src/main.py

deactivate
popd