#!/bin/bash

#init gpio mode
gpio mode 28 out

#Unlock
gpio write 28 0

#wait
sleep 5

#Lock
gpio write 28 1

exit
