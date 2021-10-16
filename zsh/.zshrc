
###############################################################
#>     __                _      <> Zsh config                <#
#>    / /   __  ___   __(_)___  <> Bardia Jedi               <#
#>   / /   / / / / | / / /_  /  <>                           <#
#>  / /___/ /_/ /| |/ / / / /_  <>                           <#
#> /_____/\__,_/ |___/_/ /___/  <> https://github.com/luviz  <#
#>                              <>                           <#
############################################################### 

## ALIASES 
## list
alias ls='exa -l --sort type'
alias lt='exa -lT --sort type'
alias ll='exa -la --sort type'
alias la='exa -a --sort type'

alias grep='grep --color=always'
alias egrep='grep --color=always -e'

## HISTORY
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

setopt autocd extendedglob nomatch notify
unsetopt beep

# bindkey -v

bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line
bindkey "^[[3~" delete-char

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/bardia/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

## STARSHIP 
eval "$(starship init zsh)"

    
