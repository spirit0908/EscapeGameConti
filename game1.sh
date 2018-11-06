#!/bin/bash

# Question 1i
echo "Quel est le film le plus détesté du Père Noël ?"
read -p '> ' string

#echo $string | iconv -f utf8 -t ascii//TRANSLIT\

shopt -s nocasematch

if [[ "$string" =~ "Le pere noel est une ordure" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

# Question 2
echo "Quel est le nom du renne du mois?"
read -p '> ' string

if [[ "$string" =~ "Comète" ]] || [[ "$string" =~ "Comet" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

#Question 3
echo "Quel est le menu du Père Noël pour le soir de Noël?"
read -p '> ' string

if [[ "$string" =~ "pizza" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

exit 0
