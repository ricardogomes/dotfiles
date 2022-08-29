from libqtile import widget
from libqtile.lazy import lazy

from modules.themes.current import palette
from modules.themes.current import fontinfo

rofi = "rofi -no-lazy-grab -show drun -modi drun"

groupbox = [
    widget.GroupBox,
    {
        "active": palette[0],
        "block_highlight_text_color": palette[1],
        "disable_drag": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"] + 20,
        "foreground": palette[2],
        "hide_unused": False,
        "highlight_color": [palette[0], palette[3]],
        "highlight_method": "block",
        "inactive": palette[0],
        "padding": fontinfo["padding"],
        "rounded": True,
        "spacing": 5,
        "this_current_screen_border": palette[4],
        "urgent_alert_method": "block",
        "urgent_border": palette[7],
        "urgent_text": palette[7],
        "use_mouse_wheel": False,
    },
]

windowname = [
    widget.WindowName,
    {
        "background": palette[2],
        "center_aligned": False,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "format": "{name}",
        "max_chars": 35,
        "padding": 3,
    },
]

currentLayoutName = [
    widget.CurrentLayout,
    {
        "background": palette[2],
        "center_aligned": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "format": "{name}",
        "max_chars": 35,
        "padding": 3,
    },
]

systray = [
    widget.Systray,
    {
        "background": palette[2],
        "foreground": palette[5],
    },
]

spacer_small = [
    widget.Spacer,
    {
        "length": 5,
        # these values are used by style func, not qtile
        "inheirit": True,
        "is_spacer": True,
        "use_separator": False,
    },
]

logo = [
    widget.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[8],
        "fontsize": fontinfo["fontsize"] * 1.8,
        "foreground": palette[1],
        "mouse_callbacks": {"Button1": lazy.spawn(rofi)},
        "padding": -2,
        "text": " \uf313 ",
    },
]

layout = [
    widget.CurrentLayoutIcon,
    {
        **fontinfo,
        "background": palette[3],
        "foreground": palette[1],
        "custom_icon_paths": "./icons",
        "scale": 0.63,
    },
]

cpu = [
    widget.CPU,
    {
        **fontinfo,
        "background": palette[10],
        "foreground": palette[1],
        "format": "\uf2db {load_percent}%",
    },
]

net = [
    widget.Net,
    {
        **fontinfo,
        "background": palette[4],
        "format": "\u2193 {down} \u2191 {up}",
        "interface": "wlan0",
        "update_interval": 3,
    },
]

mem = [
    widget.Memory,
    {
        **fontinfo,
        "format": "\uf85a {MemUsed:.2f}/{MemTotal:.2f}{mm}",
        "measure_mem": "G",
        "update_interval": 1.0,
    },
]

batt = [
    widget.Battery,
    {
        **fontinfo,
        "background": palette[5],
        "foreground": palette[1],
        "charge_char": "\uf583 ",
        "discharge_char": "",
        "empty_char": "\uf244 ",
        "format": "{char} {percent:2.0%} ({watt:.2f}W) ",
        "full_char": "\uf240 ",
        "low_background": palette[7],
        "low_foreground": palette[1],
        "low_percentage": 0.30,
        "show_short_text": False,
        "unknown_char": "\uf590 ",
    }
]

volume = [
    widget.Volume,
    {
        "foreground" : palette[1],
        "background" : palette[7],
        "fmt" : 'Vol: {}',
        "padding" : 5
    },
]

datetime = [
    widget.Clock,
    {
        **fontinfo,
        "background": palette[6],
        "foreground": palette[1],
        "format": "%B %d, %H:%M",
    },
]



