#! /bin/bash

## Push zshrc
cp ./zsh/zshrc ~/.zshrc

## starship
cp ./starship/starship.toml ~/.config/starship.toml

## qtile
cp -r ./qtile/* ~/.config/qtile/

## alacritty
mkdir -p ~/.config/alacritty/
cp ./alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml

## fish 
mkdir -p ~/.config/fish/
cp ./fish/config.fish ~/.config/fish/config.fish 

## picom
mkdir -p ~/.config/picom
cp ./picom/* ~/.config/picom/
