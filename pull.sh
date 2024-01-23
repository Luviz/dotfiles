#! /bin/bash

## starship 
mkdir -p ./starship
cp -rf ~/.config/starship.toml ./starship/

## qtile
mkdir -p ./qtile
cp -rdf ~/.config/qtile .

## alacritty
mkdir -p ./alacritty
cp -rf ~/.config/alacritty/alacritty.toml ./alacritty/alacritty.toml

## fish
mkdir -p ./fish
cp -rdf ~/.config/fish .

## picom
mkdir -p ./picom
cp ~/.config/picom/* ./picom/
