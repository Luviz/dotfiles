#! /bin/bash

## Push zshrc
cp ./zsh/zshrc ~/.zshrc

## starship
cp ./starship/starship.toml ~/.config/starship.toml

## qtile
cp -r ./qtile/* ~/.config/qtile/