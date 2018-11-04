#!/bin/bash

# Question 1i
echo "Quel est le film le plus détesté du Père Noël ?"
echo "What is the Santa Claus most hated movie?"
read -p '> ' string

if [ "$string" = "Le pere noel est une ordure" ]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

# Question 2
echo "Quel est le nom du renne du mois?"
echo "What is the name of the month's renne?"
read -p '> ' string

if [ "$string" = "Comète" ] || [ "$string" = "Comet" ]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

#Question 3
echo "Quel est le menu du Père Noël pour le soir de Noël?"
echo "When will Santa Claus eat for Christmas?"
read -p '> ' string

if [ "$string" = "pizza" ]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

exit 0
