#! /bin/bash

## Push zshrc
cp ./zsh/zshrc ~/.zshrc

## starship
cp ./starship/starship.toml ~/.config/starship.toml

## qtile
cp -r ./qtile/* ~/.config/qtile/

## alacritty
mkdir -p ~/.config/alacritty/
cp ./alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml