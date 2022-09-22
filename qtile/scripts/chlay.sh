#! /bin/bash

currentLayout=$(setxkbmap -query | grep layout | sed "s/.* //")

if [ "$currentLayout" == "us" ]
then
    setxkbmap -layout se
    notify-send "Keybord set se"
else
    setxkbmap -layout us
    notify-send "Keybord set us"
fi
