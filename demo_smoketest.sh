#!/bin/sh

DATA_DIR=./smoketests/endtoend

echo "Running smoketest..."
python bin/opengem --config_file $DATA_DIR/config.gem $@
