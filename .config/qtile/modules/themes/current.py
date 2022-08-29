#
# Current Theme Construction
# Note: choose components in imports 

from modules.themes.catppuccin  import colorPalette as currentColorPalette
from modules.themes.fonts       import victorMonoNF as currentFont
from modules.themes.fonts       import fontInfo1    as currentFontInfo

palette = currentColorPalette
fontinfo = currentFontInfo
fontinfo["font"] = currentFont
