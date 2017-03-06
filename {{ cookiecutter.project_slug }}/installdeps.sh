#!/bin/bash

set -o nounset -o errexit


PYLIBS="libs"


pip install --target "$PYLIBS" -r requirements.txt
npm install
