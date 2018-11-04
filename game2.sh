#!/bin/bash

# Question 1
echo "   13-8+13+0+7"
echo "   3+5+10-9+10+1-7-12+18 ="
echo "   _ _ _ _ _"
echo "   _ _ _ _ _ _ _ _ _"
read -p '> ' string

if [ "$string" = "MERRY CHRISTMAS" ] || [ "$string" = "merry christmas" ]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

exit 0
