#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}



#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
blueman-applet &
#flameshot &
#picom --config $HOME/.config/picom/picom.conf &
picom --config .config/picom/picom-blur.conf --experimental-backends &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
feh --randomize --bg-fill /usr/share/wallpapers/garuda-wallpapers/*
#starting user applications at boot time
run volumeicon &
#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &

## Autolocj screen
xss-lock -- i3lock -i /usr/share/wallpapers/garuda-wallpapers/Metall-SGS.png &


## Keyborad 
# echo 3 > /sys/class/leds/asus::kbd_backlight/bright4
xinput set-prop 17 --type=int 'libinput Natural Scrolling Enabled' 1
xinput set-prop 17 --type=int 'libinput Tapping Button Mapping Enabled' 1, 0
xinput set-prop 17 --type=int 'libinput Click Method Enabled' 0, 1