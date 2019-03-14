#!/bin/sh

echo "Running .xinitrc"


[ -f ~/.Xmodmap ] && xmodmap ~/.Xmodmap
[ -f ~/.Xresources ] && xrdb -merge ~/.Xresources

#########xset r rate 200 50


xrandr --setprovideroutputsource modsetting NVIDIA-0
xrandr --auto
xrandr --dpi 96

exec i3
