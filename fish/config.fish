
set parent_proc_name (ps -p $fish_pid -o ppid= |xargs -I {} ps -p {} -o comm | grep -v COMM)

if [ $parent_proc_name = 'alacritty' ]
    neofetch
end

if status is-interactive
    # Commands to run in interactive sessions can go here
end

alias ls="eza -l"
alias la="eza -la"
alias lt="eza -lT"
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

fish_add_path $HOME/.cargo/bin

## PyEnv
set -Ux PYENV_ROOT $HOME/.pyenv
set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths

# Load pyenv automatically by appending
# the following to ~/.config/fish/config.fish:

pyenv init - | source
