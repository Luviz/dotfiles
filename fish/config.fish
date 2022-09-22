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

abbr -a -g gd git pull
abbr -a -g gu git push

abbr -a -g gst git stash
abbr -a -g gstp git stash pop

abbr -a -g glog git log --oneline


alias code="code-insiders"

## K8S

abbr -a -g k kubectl

abbr -a -g kc kubectl create
abbr -a -g kd kubectl delete
abbr -a -g kg kubectl get
abbr -a -g ki kubectl describe

abbr -a -g kpod kubectl get pod 

starship init fish | source
