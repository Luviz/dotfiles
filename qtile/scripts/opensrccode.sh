#!/bin/bash
srcdirpath="/home/bardia/src/"

code="code-insiders" 
# code="code" 

selection=$(ls $srcdirpath | dmenu -l 5)

$code $srcdirpath$selection
# meh