#!/bin/bash

## ZSH
echo zsh...
stow -v -R --adopt --target="$HOME/.config/" zsh

## starship
echo starship...
stow -v -R --adopt --target="$HOME/.config/" starship

## alacritty
echo alacritty...
stow -v -R --adopt --target="$HOME/.config/alacritty" alacritty


## fish
echo fish...
stow -v -R --adopt --target="$HOME/.config/fish" fish


## picom
echo picom...
stow -v -R --adopt --target="$HOME/.config/picom" picom


## qTile

echo qtile...
stow -v -R --adopt --target="$HOME/.config/qtile" qtile
