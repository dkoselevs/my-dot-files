import os 
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

# colors = [["#282c34", "#282c34"],
          # ["#1c1f24", "#1c1f24"],
          # ["#dfdfdf", "#dfdfdf"],
          # ["#ff6c6b", "#ff6c6b"],
          # ["#98be65", "#98be65"],
          # ["#da8548", "#da8548"],
          # ["#51afef", "#51afef"],
          # ["#c678dd", "#c678dd"],
          # ["#46d9ff", "#46d9ff"],
          # ["#a9a1e1", "#a9a1e1"]]

colors = ["#282828",
          "#1d2021",
          "#928374",
          "#cc241d",
          "#98971a",
          "#d65d0e",
          "#458588",
          "#b16286",
          "#689d6a",
          "#a9a1e1"]

font_color = "#fbf1c7"


keys = [
    #Sound
    Key([mod], "XF86AudioMute", lazy.spawn("amixer -q -D pulse sset Master toggle")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    #Keyboard layout
    Key([mod], "F1", lazy.spawn('setxkbmap -layout us')),
    Key([mod], "F2", lazy.spawn('setxkbmap -layout ru')),
    Key([mod], "F3", lazy.spawn('setxkbmap -layout lv')),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]
groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
##
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus='#fbf1c7', border_normal='#a89984', border_width=4, margin=12),
    layout.Max(margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(border_focus='#fbf1c7', border_normal='#a89984', border_width=4, margin=8),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(columnwidth=210),
]

widget_defaults = dict(
    font='Ubuntu',
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper ='~/Wallpapers/main.jpg',
        wallpaper_mode='stretch',
        # top=bar.Bar(
            # [widget.Sep(
                       # linewidth = 0,
                       # padding = 6,
                       # foreground = colors[2],
                       # background = colors[0]
                       # ),
              # widget.Sep(
                       # linewidth = 0,
                       # padding = 6,
                       # foreground = colors[2],
                       # background = colors[0]
                       # ),
              # widget.GroupBox(
                       # font = "Ubuntu",
                       # fontsize = 16,
                       # margin_y = 5,
                       # margin_x = 0,
                       # padding_y = 5,
                       # padding_x = 3,
                       # borderwidth = 3,
                       # active = colors[2],
                       # active = "#fbf1c7",
                       # inactive = "#fbf1c7",
                       # rounded = False,
                       # highlight_color = colors[1],
                       # highlight_method = "line",
                       # this_current_screen_border = colors[6],
                       # this_screen_border = colors [4],
                       # other_current_screen_border = colors[6],
                       # other_screen_border = colors[4],
                       # foreground = "#fbf1c7",
                       # background = colors[0]
                       # ),
             # widget.TextBox(
                       # text = '| ',
                       # font = "Ubuntu Mono",
                       # background = colors[0],
                       # foreground = '474747',
                       # padding = 2,
                       # ),
              # widget.WindowName(
                       # foreground = "#fbf1c7",
                       # background = colors[0],
                       # padding = 0
                       # ),
              # widget.Systray(
                       # background = colors[0],
                       # padding = 5
                       # ),
              # widget.Sep(
                       # linewidth = 0,
                       # padding = 6,
                       # foreground = colors[0],
                       # background = colors[0]
                       # ),
              # widget.CurrentLayout(
                       # background=colors[0],
                       # foreground="#fbf1c7"
                      # ),
              # widget.TextBox(
                       # text = '| ',
                       # font = "Ubuntu Mono",
                       # background = colors[0],
                       # foreground = '474747',
                       # padding = 2,
                       # ),
              # widget.ThermalSensor(
                       # foreground = font_color,
                       # background = colors[0],
                       # threshold = 90,
                       # fmt = 'Temp: {}',
                       # padding = 5
                       # ),
              # widget.TextBox(
                       # text = '| ',
                       # font = "Ubuntu Mono",
                       # background = colors[0],
                       # foreground = '474747',
                       # padding = 2,
                       # ),
              # widget.PulseVolume(
                       # foreground = font_color,
                       # background = colors[0],
                       # fmt = 'Vol: {}',
                       # padding = 5
                       # ),
              # widget.TextBox(
                       # text = '| ',
                       # font = "Ubuntu Mono",
                       # background = colors[0],
                       # foreground = '474747',
                       # padding = 2,
                       # ),
              # widget.KeyboardLayout(
                       # foreground = font_color,
                       # background = colors[0],
                       # fmt = 'Keyboard: {}',
                       # padding = 5
                       # ),
              # widget.TextBox(
                       # text = '| ',
                       # font = "Ubuntu Mono",
                       # background = colors[0],
                       # foreground = '474747',
                       # padding = 2,
                       # ),
              # widget.Clock(
                       # foreground = font_color,
                       # background = colors[0],
                       # format = "%A, %B %d - %H:%M "
                       # ),
            # ],
            # 24
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    ),
]
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

#Drag floating layouts.
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/polybar/forest/launch.sh')
    subprocess.run([home])
    lazy.spawncmd("~/.config/rofi/launchers/text/launcher.sh", shell=True)


auto_fullscreen = True
# focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
