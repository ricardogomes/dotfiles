"""

    Qtile Config File
    Docs: https://docs.qtile.org/en/stable/index.html

"""
from libqtile.log_utils import logger

from modules.settings import *
from modules.hooks import *
from modules.layouts import *
from modules.groups import * 
from modules.keymaps import *

from modules.statusbar import extension_defaults, screens, widget_defaults

logger.warning("[DEBUG] Reading config")

