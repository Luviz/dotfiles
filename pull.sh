#! /bin/bash

## starship 
mkdir -p ./starship
cp -rf ~/.config/starship.toml ./starship/

## qtile
mkdir -p ./qtile
cp -rf ~/.config/qtile .

## alacritty
mkdir -p ./alacritty
cp -rf ~/.config/alacritty/alacritty.yml ./alacritty/alacritty.yml

## fish
mkdir -p ./fish
cp ~/.config/fish/config.fish ./fish/config.fish

## picom
mkdir -p ./picom
cp ~/.config/picom/* ./picom/
