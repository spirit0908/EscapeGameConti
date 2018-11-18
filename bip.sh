#!/bin/bash

gpio mode 27 out

gpio write 27 1

sleep 0.2

gpio write 27 0

 
