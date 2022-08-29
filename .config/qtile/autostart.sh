#!/bin/bash

# 
# Qtile Autostart Script
# Obejctives:
#   - apply propper screen layout
#   - run one time apps (nitrogen --restore)
#   - start apps
# 

not_running() {
  echo "$ts: checking $1"
  [ "$1" = "" ]  && return 0
  [ `pgrep -n $1` ] && return 1 || return 0
}
MONITORS=$(xrandr --listactivemonitors | head -n1 | cut -d ' ' -f 2)
SECOND_WIDTH=$(xrandr --listactivemonitors | tail -n1 | cut -d ' ' -f 4 | cut -d '/' -f1)

if [ $MONITORS == "2" ]
then
  # Multiple Screens - For now assuming Home setup
  # TODO: Support Classes and Work Office setup
  ~/.screenlayout/home.sh
  if (( $SECOND_WIDTH > 3000 ))
  then
    # Home Setup
    if not_running synergy
    then
      synergy &
    fi
  fi
fi

if not_running "picom"
then
  picom -b
fi

nitrogen --restore &
