"""

    Qtile Settings (except default widgets, default floating layout)
    Docs: https://docs.qtile.org/en/stable/manual/config/index.html#configuration-variables

"""
auto_fullscreen             = True
auto_minimize               = False
bring_front_click           = False
cursor_warp                 = False
dgroups_app_rules           = []  # type: list
dgroups_key_binder          = None
focus_on_window_activation  = "smart"
follow_mouse_focus          = True
reconfigure_screens         = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
