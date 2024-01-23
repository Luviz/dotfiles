
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
alias ls='ls --color'
alias ll='ls -la'
alias la='ls -a'
# echo "ls"

if type eza > /dev/null; then
    # echo "eza"
    alias ls='eza -l --sort type'
    alias lt='eza -lT --sort type'
    alias ll='eza -la --sort type'
    alias la='eza -a --sort type'
fi

alias grep='grep --color=always'
alias egrep='grep -e'

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

# The following lines were added by compinstall
zstyle :compinstall filename '/home/bardia/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

## STARSHIP 
eval "$(starship init zsh)"

    
