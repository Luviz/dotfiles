neofetch

if status is-interactive
    # Commands to run in interactive sessions can go here
end

alias ls="exa -l"
alias la="exa -la"
alias lt="exa -lT"
# alias cat="bat"

abbr -a -g gco git checkout
abbr -a -g gcob git checkout -b

abbr -a -g gst git stash
abbr -a -g gstp git stash pop

abbr -a -g glog git log --oneline


alias code="code-insiders"

starship init fish | source
