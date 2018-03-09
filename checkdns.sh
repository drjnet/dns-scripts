#!/bin/bash

# Quick script to check current dns for domain

function mainLoop () {
  echo -e "\n---Checking common records on dns zone : $1----"
  
  echo -e "Checking name servers"
  dig +short ns $1

  echo -e "\nChecking main a record"
  dig +short a $1

  echo -e "\nChecking www pointer"
  dig +short a www.$1

  echo -e "\nChecking mx records"
  dig +short mx $1

  echo -e "\nChecking txt records"
  dig +short txt $1
}

function actionKeys () {
  echo -e "\nDo you want a detail record? Enter (a),(w)ww,(m)x,t(xt) or e(x)it. \n"

  read more

  if [ $more == "a" ]; then
    echo -e "Executing : dig a $1"
    dig a $1
    exit 1
  elif [ $more == "w" ]; then
    echo -e "Executing : dig www $1"
    dig a www.$1
    exit 1
  elif [ $more == "m" ]; then
    echo -e "Executing : dig mx $1"
    dig mx $1
    exit 1
  elif [ $more == "t" ]; then
    echo -e "Executing : dig mx $1"
    dig mx $1
    exit 1
  else
    exit 1  
  fi
}

# Check for script params
if [ -z "$1" ]
  then
    echo "Parameter missing, usage : checkdns domain.com "
fi

# Main loop
while :
do
  clear
  mainLoop $1
  actionKeys $1
done





