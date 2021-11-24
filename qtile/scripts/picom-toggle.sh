#!/bin/bash
if pgrep -x "picom" > /dev/null
then
	killall picom
else
	picom -b --backend glx --experimental-backends
fi
