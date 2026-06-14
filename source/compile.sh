#!/usr/bin/env bash

cd "$(dirname "$0")"

python2 compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9

read -p "Press enter to close..."
