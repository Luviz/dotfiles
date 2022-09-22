#! /bin/bash

currentLayout=$(setxkbmap -query | grep layout | sed "s/.* //")

if [ "$currentLayout" == "us" ]
then
    setxkbmap -layout se
    notify-send "Keyboard set SE"
else
    setxkbmap -layout us
    notify-send "Keyboard set US"
fi
