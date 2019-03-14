#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -U $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar, using default config location ~/.config/polybar/config

#if type "xrandr"; then
#	for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#		MONITOR=$m polybar --reload top &
#	done
#else
#	polybar --reload large &
#fi

polybar --reload top &
polybar --reload large  &


echo "Polybar launched..."
