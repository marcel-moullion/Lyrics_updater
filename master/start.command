#!/bin/bash

cd "${ cd "${dirname "$0"}" </dev/null 2>&1 ; pwd -P }"
python updateFiles.py

read -n 1 -s -r -p "Press any key to continue"