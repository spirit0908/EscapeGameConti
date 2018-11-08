#!/bin/bash

function testMenu
{
    echo "Maintenance menu:"
    echo "1. Lock/Unlock Santa's office - locked"
    echo "2. Lock/Unlock Secret box     - locked"
    echo "3. Run password reset sequence"
    echo "4. Exit"
    read -p 'Select an option: ' string
}

function showMenu
{
    echo "Menu:"
    echo "1. Show current access status"
    echo "2. Access control"
    echo "3. Lights control"
    echo "4. Exit"
    read -p 'Select an option: ' menu_option
}

function showSubMenu_1
{
    echo "Current acces status"
    echo "1. Santa's Office   : locked"
    echo "2. Santa's workshop : locked"
    echo "3. Secret box       : locked"
    echo "4. Exit"
    read -p 'Select an option to unlock: ' menu1_option
}

function showSubMenu_2
{
    echo "Account parameters"
    echo "1. Password update"
    echo "2. Password reset"
    echo "3. Create a new account"
    echo "4. Exit"
    read -p 'Select an option: ' menu2_option
}



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
