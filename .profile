#!/bin/bash
###
#
#  Profile file. Runs on login and defines the system wide configurations
#
###


# Adds `~/.scripts` and all subdirectories to $PATH
# export PATH="$PATH:$(du "$HOME/.scripts/" | cut -f2 | tr '\n' ':')"

echo "Sourcing .profile"

export PATH=$PATH:$HOME/spells:/usr/bin/:/usr/local/bin

export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="firefox"
export READER="zathura"
export FILE="ranger"

export XDG_CONFIG_HOME=$HOME/.config
export XDG_CONFIG_DIRS=$XDG_CONFIG_HOME:$HOME

# less/man colors
export LESS=-R
export LESS_TERMCAP_mb=$'\E[1;31m'     # begin bold
export LESS_TERMCAP_md=$'\E[1;36m'     # begin blink
export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
export LESS_TERMCAP_so=$'\E[01;44;33m' # begin reverse video
export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
export LESS_TERMCAP_ue=$'\E[0m'        # reset underline


#echo "$0" | grep "bash$" >/dev/null && [ -f ~/.bashrc ] && source "$HOME/.bashrc"

# Start graphical server if i3 not already running.
[ "$(tty)" = "/dev/tty1" ] && ! pgrep -x i3 >/dev/null && exec startx

# NOT USED VOIDRICE CONFIGS 

#export BIB="$HOME/Documents/LaTeX/uni.bib"
#export REFER="$HOME/.referbib"
#export SUDO_ASKPASS="$HOME/.scripts/tools/dmenupass"
#export PIX="$HOME/.pix/"

# Switch escape and caps if tty:
#sudo -n loadkeys ~/.scripts/ttymaps.kmap 2>/dev/null
