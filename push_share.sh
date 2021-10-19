#! /bin/bash

mkdir -p /usr/share/wallpapers/bardia/
mkdir -p /usr/share/icons/bardia/
mkdir -p /usr/share/wallpapers/bardia/lockscreen

cp ./wallpapers/* /usr/share/wallpapers/bardia/
cp ./icons/* /usr/share/icons/bardia/


## create i3lock compatible image
filename='ink_in_water'
convert -resize $(xdpyinfo | grep dimensions | cut -d\  -f7 | cut -dx -f1) ./wallpapers/$filename.jpg /usr/share/wallpapers/bardia/lockscreen/$filename.png