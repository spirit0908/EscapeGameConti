#!/bin/bash

#Lockdown
./unlock.sh

#Launch NFC reader
./NFC_read.sh &

#Launch GUI
python3 EscapeGameConti.py
