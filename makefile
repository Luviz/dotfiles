HOME_DIR := $(HOME)
CONFIG_DIR := $(HOME_DIR)/.config

DATE := $(shell date +"%Y%m%d_%H%M%S")

init:
	@echo Run options below:
	@echo "$$ make STOW   - stow init config stowing"
	@echo "$$ make RESTOW - restow config file (used to clean up unused files)"
	git stage --all


STOW: PRE_STOW STOW_GIT STOW_ZSH STOW_STARSHIP STOW_ALACRITTY STOW_FISH STOW_PICOM STOW_QTILE POST_STOW

PRE_STOW:
	@echo Stowing...
	@mkdir -p $(CONFIG_DIR)
	@mkdir -p tmp
	git stage --all

POST_STOW: 
	git diff > ./tmp/$(DATE).patch
	git restore .
	git reset
	@echo Stowing Completed...

STOW_GIT: 
	@echo stowing git...
	stow -v --adopt --target="$(HOME_DIR)/" git
	@echo =====================================


STOW_ZSH: 
	@echo stowing zsh...
	stow -v --adopt --target="$(CONFIG_DIR)/" zsh
	@echo =====================================

STOW_STARSHIP:
	@echo starship...
	stow -v --adopt --target="$(CONFIG_DIR)/" starship
	@echo =====================================

STOW_ALACRITTY:
	@echo alacritty...
	@mkdir -p $(CONFIG_DIR)/alacritty
	stow -v --adopt --target="$(CONFIG_DIR)/alacritty" alacritty
	@echo =====================================


STOW_FISH:
	@echo fish...
	@mkdir -p $(CONFIG_DIR)/fish
	stow -v --adopt --target="$(CONFIG_DIR)/fish" fish
	@echo =====================================


STOW_PICOM:
	@echo picom...
	@mkdir -p $(CONFIG_DIR)/picom
	stow -v --adopt --target="$(CONFIG_DIR)/picom" picom
	@echo =====================================


STOW_QTILE:
	@echo qtile...
	@mkdir -p $(CONFIG_DIR)/qtile
	stow -v --adopt --target="$(CONFIG_DIR)/qtile" qtile
	@echo =====================================



RESTOW: RESTOW_GIT RESTOW_ZSH RESTOW_STARSHIP RESTOW_ALACRITTY RESTOW_FISH RESTOW_PICOM RESTOW_QTILE

RESTOW_GIT: 
	@echo restowing git...
	stow -v -R --adopt --target="$(HOME_DIR)/" git
	@echo =====================================


RESTOW_ZSH: 
	@echo restowing zsh...
	stow -v -R --adopt --target="$(CONFIG_DIR)/" zsh
	@echo =====================================

RESTOW_STARSHIP:
	@echo restowing starship...
	stow -v -R --adopt --target="$(CONFIG_DIR)/" starship
	@echo =====================================

RESTOW_ALACRITTY:
	@echo restowing alacritty...
	stow -v -R --adopt --target="$(CONFIG_DIR)/alacritty" alacritty
	@echo =====================================


RESTOW_FISH:
	@echo restowing fish...
	stow -v -R --adopt --target="$(CONFIG_DIR)/fish" fish
	@echo =====================================


RESTOW_PICOM:
	@echo restowing picom...
	stow -v -R --adopt --target="$(CONFIG_DIR)/picom" picom
	@echo =====================================


RESTOW_QTILE:
	@echo restowing qtile...
	stow -v -R --adopt --target="$(CONFIG_DIR)/qtile" qtile
	@echo =====================================
