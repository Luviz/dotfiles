#! /bin/bash

sudo mkdir -p /usr/share/wallpapers/bardia/
sudo mkdir -p /usr/share/icons/bardia/
sudo mkdir -p /usr/share/wallpapers/bardia/lockscreen

sudo cp ./wallpapers/* /usr/share/wallpapers/bardia/
sudo cp ./icons/* /usr/share/icons/bardia/


## create i3lock compatible image
filename='ink_in_water'
sudo convert -resize $(xdpyinfo | grep dimensions | cut -d\  -f7 | cut -dx -f1) ./wallpapers/$filename.jpg /usr/share/wallpapers/bardia/lockscreen/$filename.png