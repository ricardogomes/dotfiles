#!/bin/bash
###
# .basrc
#
# Runs for every interactive shell (login or not do to being sourced in .bash_profile)
# 
# Purpose: define BASH related running configurations
# Notes:
#	- some elements where extracted to other files under .config/shell
###


# If not running interactively, don't do anything
[[ $- != *i* ]] && return

echo "Sourcing .bashrc"

###
# BASH CONFIGURATIONS
###

HISTCONTROL=ignoredups		# Ignore sequential duplicates
HISTSIZE= HISTFILESIZE= 	# Infinite history.
shopt -s histappend		# Append instead of replacing
shopt -s checkwinsize		# Check window size and redefine lines and columns if necessary
shopt -s autocd 		#Allows you to cd into directory merely by typing the directory name.

# Needs review
stty -ixon # Disable ctrl-s and ctrl-q.
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\h \[$(tput setaf 5)\]\W\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"


if [[ -d /usr/share/bash_completion/completions ]]; then
	for file in /usr/share/bash_completion/completions/* ; do
		# shellcheck source=/dev/null
		source "$file"
	done
fi
unset file




###
# ALIASES
###

source $XDG_CONFIG_HOME/shell/aliases
source $XDG_CONFIG_HOME/shell/arch_aliases
source $XDG_CONFIG_HOME/shell/i3_aliases

# FUNCTIONS

test_function() { echo "running function with arguments $@" ;}




