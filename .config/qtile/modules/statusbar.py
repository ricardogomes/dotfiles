# credits: the-argus
# TODO: my own statusbar, use this to setup qtile for now.

from libqtile import bar, qtile, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from modules.themes.current import palette
from modules.themes.current import fontinfo
from modules.statusbar_widgets import groupbox, windowname, currentLayoutName, systray, spacer_small, logo, layout, cpu, net, mem, batt, volume, datetime


borderline = dict(
    border_focus=palette[8],
    border_normal=palette[1],
    border_width=1,
    margin=4,
)



def widgetlist():
    return [
        spacer_small,
        logo,
        groupbox,
        layout,
        windowname,
        cpu,
        mem,
        batt,
        volume,
        datetime,
        systray,
    ]

def widgetlistsecondary():
    return [
        spacer_small,
        logo,
        groupbox,
        layout,
        currentLayoutName,
        windowname,
        datetime,
    ]


def style(widgetlist):
    styled = widgetlist[:]

    for index, wid in enumerate(widgetlist):
        end_sep = {
            "font": fontinfo["font"],
            "fontsize": 34,
            "padding": -1,
            "text": " \ue0b6",
        }

        if index < len(widgetlist) - 1:
            # end_sep["background"]=widgetlist[index+1][1].get("background", palette[1])
            # end_sep["foreground"]=wid[1].get("background", palette[1])

            end_sep["foreground"] = widgetlist[index + 1][1].get(
                "background", palette[1]
            )
            end_sep["background"] = wid[1].get("background", palette[1])

            if wid[1].get("is_spacer") and wid[1].get("inheirit"):
                bg = widgetlist[index + 1][1].get("background", palette[1])
                wid[1]["background"] = bg
                end_sep["background"] = bg

            # insert separator before current
            if wid[1].get("use_separator", True):
                styled.insert(styled.index(wid) + 1, (widget.TextBox, end_sep))

    return [w[0](**w[1]) for w in styled]


def my_bar():
    return bar.Bar(
        [*style(widgetlist())],
        34,
        foreground=palette[0],
        background=palette[1],
        opacity=1,
        margin=[
            borderline["margin"],
            borderline["margin"],
            borderline["border_width"],
            borderline["margin"],
        ],
    )

def my_bar_secondary():
    return bar.Bar(
        [*style(widgetlistsecondary())],
        34,
        foreground=palette[0],
        background=palette[1],
        opacity=1.0,
        margin=[
            borderline["margin"],
            borderline["margin"],
            borderline["border_width"],
            borderline["margin"],
        ],
    )

widget_defaults = dict(
    **fontinfo,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=my_bar()),
    Screen(top=my_bar_secondary()),
]

