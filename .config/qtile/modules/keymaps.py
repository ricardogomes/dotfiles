"""

    Qtile Keymaps File
    Docs: https://docs.qtile.org/en/stable/manual/config/index.html#key-bindings

"""
from libqtile.command import lazy
from libqtile.config import EzClick, EzDrag, EzKey

from modules.apps import * 


EzKey.modifier_keys = {
    "M": "mod4",
    "A": "mod1",
    "S": "shift",
    "C": "control",
    "H": "mod3",
}

window_navigation = [
    EzKey("M-h",            lazy.layout.left()),
    EzKey("M-j",            lazy.layout.down()),
    EzKey("M-k",            lazy.layout.up()),
    EzKey("M-l",            lazy.layout.right()),

    EzKey("M-<Left>",       lazy.layout.left()),
    EzKey("M-<Down>",       lazy.layout.down()),
    EzKey("M-<Up>",         lazy.layout.up()),
    EzKey("M-<Right>",      lazy.layout.right()),
    
    EzKey("M-<Tab>",        lazy.layout.next()),
]

window_displacement = [
    EzKey("M-S-h",          lazy.layout.swap_left(), lazy.layout.shuffle_left()),
    EzKey("M-S-j",          lazy.layout.swap_down(), lazy.layout.shuffle_down()),
    EzKey("M-S-k",          lazy.layout.swap_up(), lazy.layout.shuffle_up()),
    EzKey("M-S-l",          lazy.layout.swap_right(), lazy.layout.shuffle_right()),
    
    EzKey("M-S-<Left>",     lazy.layout.swap_left(), lazy.layout.shuffle_left()),
    EzKey("M-S-<Down>",     lazy.layout.swap_down(), lazy.layout.shuffle_down()),
    EzKey("M-S-<Up>",       lazy.layout.swap_up(), lazy.layout.shuffle_up()),
    EzKey("M-S-<Right>",    lazy.layout.swap_right(), lazy.layout.shuffle_right()),

]

window_size_control = [
    EzKey("M-C-j",          lazy.layout.shrink()),
    EzKey("M-C-k",          lazy.layout.grow()),
  
    EzKey("M-C-<Down>",     lazy.layout.shrink()),
    EzKey("M-C-<Up>",       lazy.layout.grow()),

    EzKey("M-C-n",          lazy.layout.normalize()),  # Restore to original size
    EzKey("M-C-f",          lazy.layout.maximize()),  
]

toggles = [
    EzKey("M-q", lazy.window.kill()),
    EzKey("M-l", lazy.next_layout()),
    EzKey("M-f", lazy.window.toggle_fullscreen()),
    EzKey("M-t", lazy.window.toggle_floating()),
]

qtile_controls = [
    EzKey("M-S-r", lazy.restart()),
]

rofi_spawns = [
    EzKey("M-<space>", lazy.spawn("rofi -show drun")),
    EzKey("M-S-<space>", lazy.spawn("rofi -show run")),
    EzKey("M-C-p", lazy.spawn("/home/rg/spells/powermenu.sh")),
]

application_spawns = [
    EzKey("M-<Return>", lazy.spawn(terminal)),
    EzKey("M-b", lazy.spawn(browser)),
]

# Drag floating layouts.
mouse = [
    EzDrag(
        "M-<Button1>",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    EzDrag(
        "M-<Button3>", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    EzClick("M-<Button2>", lazy.window.bring_to_front()),
]

# Groups
group_keys = []
for i in range(10):
    group_keys.extend(
        [
            EzKey("M-%s" % i, lazy.group[str(i)].toscreen()),
            EzKey("M-S-%s" % i, lazy.window.togroup(i)),
        ]
    )

group_keys.extend([
    EzKey("M-<Home>", lazy.screen.next_group()),
    EzKey("M-<End>", lazy.screen.prev_group())
])

keys = [
    *window_navigation,
    *window_displacement,
    *window_size_control,
    *toggles,
    *qtile_controls,
    *rofi_spawns,
    *application_spawns,
    *group_keys,
]

