#
# Qtile Hooks
#
import os
import subprocess

from libqtile import hook
from libqtile.log_utils import logger

# Startup Hook that runs only once
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


# Learning Qtile Hooks
@hook.subscribe.screen_change
def after_screen_change(event):
    logger.warning("\n\t[HOOK] After Screen Change")

@hook.subscribe.restart
def before_restart():
    logger.warning("\n\t[HOOK] Before Restarting ")

@hook.subscribe.startup
def before_startup():
    logger.warning("\n\t[HOOK] Before Startup ")
