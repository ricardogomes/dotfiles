# Groups Module

from libqtile.command import lazy
from libqtile.config import DropDown, EzKey, Group, ScratchPad
from modules.keymaps import keys

from modules.themes.current import palette

groups = [
    Group(name="1", label="", layout='max'),
    Group(name="2", label="", layout='max'),
    Group(name="3", label="", layout='monadtall'),
    Group(name="4", label="", layout='monadtall'),
    Group(name="5", label="", layout='max'),
    Group(name="6", label="", layout='max'),
    Group(name="7", label="", layout='monadtall'),
    Group(name="8", label="", layout='monadtall'),
    Group(name="9", label="", layout='monadtall'),
    Group(name="0", label="", layout='monadtall'),
]

# Scratchpads
next_maximum = {
    "x": 0.225,
    "y": 0.275,
    "width": 0.55,
    "height": 0.45,
    "opacity": 1.00,
    "on_focus_lost_hide": False,
}

groups.append(
    ScratchPad("scratchpads",
        [
            DropDown("terminal", "alacritty", **next_maximum),
            DropDown("ranger", "alacritty -e ranger", **next_maximum),
        ],
    )
)

keys.extend(
    [
        EzKey("M-A-<Return>", lazy.group["scratchpads"].dropdown_toggle("terminal")),
        EzKey("M-A-r", lazy.group["scratchpads"].dropdown_toggle("ranger")),
    ]
)

