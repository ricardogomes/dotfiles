"""

    Qtile Layouts Config File
    Docs: https://docs.qtile.org/en/stable/manual/ref/layouts.html

"""
from libqtile import layout
from libqtile.config import Match

from modules.themes.current import palette


default_border = dict(
    border_focus=palette[10],
    border_normal=palette[11],
    border_width=2,
)

layouts = [
    layout.MonadTall(
        **default_border,
        ratio               = 0.7,
        margin              = 10,
        single_border_width = 0,
        single_margin       = 4
    ),
    layout.Max(
        **default_border,
        margin              = 4
    ),
]

floating_layout = layout.Floating(
    **default_border,
    float_rules=[
        *layout.Floating.default_float_rules,
        # https://github.com/qtile/qtile/blob/4c98020e14be7b022a305854a18b7a2df4cdb2eb/libqtile/layout/floating.py#L43
        Match(wm_class  = "confirmreset"),  # gitk
        Match(wm_class  = "makebranch"),  # gitk
        Match(wm_class  = "maketag"),  # gitk
        Match(title     = "branchdialog"),  # gitk
        Match(wm_class  = "pinentry"),  # GPG key password entry
        Match(title     = "Picture-in-Picture"),  # FireFox
        Match(wm_class  = "ssh-askpass"),  # ssh-askpass
    ],
)
