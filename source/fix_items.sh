#!/bin/bash


python2 process_troops.py
python2 process_init.py
python2 process_items.py

python2 process_init.py
python2 process_items.py

rm -rf *.pyc
