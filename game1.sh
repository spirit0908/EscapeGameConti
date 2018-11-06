#!/bin/bash

#Question 1
echo "Entrez votre identifiant"
read -p 'id: ' string
str=`echo $string | iconv -f utf8 -t ascii//TRANSLIT`
if [[ "$str" =~ "perenoel" ]]
then
    echo 'Bonjour Père Noël. Nous allons commencer la procédure de réinitialisation de votre mot de passe.'
else
    echo 'Identifiant invalide.'
    exit 1
fi

# Question 2
echo "Quel film detestez-vous le plus?"
read -p '> ' string
str=`echo $string | iconv -f utf8 -t ascii//TRANSLIT`

shopt -s nocasematch

if [[ "$str" =~ "le pere noel est une ordure" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

# Question 2
echo "Quel est le nom du renne du mois?"
read -p '> ' string
str=`echo $string | iconv -f utf8 -t ascii//TRANSLIT`

if [[ "$str" =~ "comete" ]] || [[ "$string" =~ "comet" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

#Question 3
echo "Quel est votre plat préféré?"
read -p '> ' string
str=`echo $string | iconv -f utf8 -t ascii//TRANSLIT`

if [[ "$str" =~ "foie gras" ]]
then
    echo 'right!'
else
    echo 'wrong...'
    exit 1
fi

#Fin
echo "Votre mot de passe a été réinitialisé avec succès !"

exit 0
