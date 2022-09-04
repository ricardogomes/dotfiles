# Qtile Configutation

This is my [Qtile](http://www.qtile.org/) configuration.

## Objectives

This configuration of Qtile as a few objectives / requirements:

**Functional**
- a normal tilling window manager
- a system bar where I can see the main indicators
- several workspaces so that I can organize my apps
- support for multiple monitors

**Extra**
- Aesthetically pleasing
- Understandable configs
  - both for me in the future and for anyone viewing this


## Keymaps

**Mod -> Super**

**Terminal:** alacritty
**Browser:** brave-nightly

|Keys     |Action               |Notes|
|----     |------               |-----|
|Mod h    |Move focus to app on left  | Still trying out vim keybindings | 
|Mod j    |Move focus to app down     | Still trying out vim keybindings | 
|Mod k    |Move focus to app up       | Still trying out vim keybindings |
|Mod l    |Move focus to app on right | Still trying out vim keybindings | 
|         |                     |     |
|Mod Left |Move focus to app on left  |     | 
|Mod Down |Move focus to app down     |     | 
|Mod Up   |Move focus to app up       |     | 
|Mod Right|Move focus to app on right |     | 
| | | 
|Mod Tab  |Move focus to the next app in the stack | |
|Mod Shift h | Move app to the left | Still trying out vim keybindings |
|Mod Shift j | Move app down | Still trying out vim keybindings |
|Mod Shift k | Move app up | Still trying out vim keybindings |
|Mod Shift l | Move app to the right | Still trying out vim keybindings |
|Mod Shift Left | Move app to the left | |
|Mod Shift Down | Move app to the down | |
|Mod Shift Up | Move app to the up | |
|Mod Shift Right | Move app to the right | |
| | | 
|Mod Ctrl j | Shrink app | Still trying out vim keybindings |
|Mod Crtl h | Grow app | Still trying out vim keybindings |
|Mod Ctrl Down | Shrink app | | 
|Mod Crtl Up | Grow app | |
|Mod Ctrl n | Go to the default layout structure | |
|Mod Ctrl f | Toggle Maximize/Minimize app | | 
| | | 
| Mod q | Close app | | 
| Mod l | Change to the next layout (Max or MonadTall) | |
| Mod f | Toggle Fullscreen on the current app | | 
| Mod t | Toggle Floating on the current app | |
| Mod Ctrl b | Toggle bar on the current app scree | |
| | |
| Mod Shift r | Restart Qtile | |
| | | 
| Mod Space | Run Rofi Applications Menu | |
| Mod Shift Space | Run Rofi Commands Menu | | 
| Mod Shift p | Run Rofi Power Menu | |
| | | 
| Mod Return | Spawn **Terminal** | |
| Mod b | Spawn **Browser** | |
| | | 
| Mod [0..9] | Change to group x | |
| Mod Shift [0..9] | Move app to group x | |
| Mod Home | Change to next group | |
| Mod End | Change to previous group | | 

## Resources

- [Qtile documentation](https://docs.qtile.org/en/stable/)


### Inspirations

- [Icy-Thought/Snowflake: NixOS Flake Configuration.](https://github.com/Icy-Thought/Snowflake)

## Backlog

- [ ] Clear logger used for learning / debugging 
- [ ] Improve autostart.sh by supporting other environments besides Home
- [ ] Improve statusbar

## Change log

- **2022-08-20 [v0.21.0]** started the documentation
- **2022-08-20 [v0.21.0]** added keymap to toggle bar
