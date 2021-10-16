
###############################################################
#>     __                _      <> QTile config              <#
#>    / /   __  ___   __(_)___  <> Bardia Jedi               <#
#>   / /   / / / / | / / /_  /  <> 2021                      <#
#>  / /___/ /_/ /| |/ / / / /_  <>                           <#
#> /_____/\__,_/ |___/_/ /___/  <> https://github.com/luviz  <#
#>                              <>                           <#
############################################################### 

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, Rule
from libqtile.command import lazy
from resize import Resize
# from libqtile.widget import BatteryIcon, BatteryState, Battery

# from libqtile.widget import Spacer

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

class Commands:
    lock_screen = "i3lock -i /usr/share/wallpapers/garuda-wallpapers/Metall-SGS.png"
    d_menu = "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


myTerm = "alacritty"  # My terminal of choice

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "e", lazy.spawn('pcmanfm')),
    Key([mod], "o", lazy.spawn(Commands.lock_screen)),
    # Key([mod], "d", lazy.spawn('nwggrid -p -o 0.4')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "x", lazy.shutdown()),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
    Key([mod, "shift"], "d", lazy.spawn(Commands.d_menu)),
    #    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"],     "q", lazy.window.kill()),
    Key([mod, "shift"],     "r", lazy.restart()),
    Key([mod, "control"],   "r", lazy.restart()),
    Key([mod, "shift"],     "x", lazy.shutdown()),

    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "o", lazy.spawn(
        home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "t", lazy.spawn('xterm')),
    # Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),

    # ALT + ... KEYS
    # Key(["mod1"], "p", lazy.spawn('pamac-manager')),
    # Key(["mod1"], "f", lazy.spawn('firedragon')),
    # Key(["mod1"], "m", lazy.spawn('pcmanfm')),
    # Key(["mod1"], "w", lazy.spawn('garuda-welcome')),
    Key(["mod1", "control"], "p", lazy.spawn('nwggrid -p -o 0.4')),


    # CONTROL + SHIFT KEYS
    Key(["control", "shift"], "Escape", lazy.spawn('lxtask')),

    # SCREENSHOTS
    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key(["control"], "Print", lazy.spawn('flameshot gui')),
    #    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

    # MULTIMEDIA KEYS

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    #    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    #    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    #    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    #    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "m", lazy.layout.maximize()),

    KeyChord([mod], "p", [
        Key([],"p", lazy.group.setlayout("max")),
        # Key([],"l", lazy.group.setlayout("treetab")), ## dose not work - side panel wont show
        Key([],"o", lazy.group.setlayout("monadtall")),
        Key([],"i", lazy.group.setlayout("monadwide")),
    ]),

    KeyChord([mod], "y", [
        Key([],"l", lazy.group.setlayout("max")),
        Key([],"o", lazy.group.setlayout("monadtall")),
        Key([], "Up", *Resize.RS_UP()),
        Key([], "Down", *Resize.RS_DOWN()),
        Key([], "Left", *Resize.RS_LEFT()),
        Key([], "Right", *Resize.RS_RIGHT()),
    ], mode="win size"),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    # Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    # Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    # Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    # Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()), 

    # LUNCH APPS
    ## DEV - lunch Code 
    KeyChord([mod], "d", [
        Key([], 'p', lazy.spawn("code /home/bardia/.config/")),
        Key([], 'd', lazy.spawn("code /home/bardia/mynotes/")),
        Key([], 'n', lazy.spawn("code -n")),
    ]),

    ## Quick App
    KeyChord([mod], "a", [
        Key([], 'a', lazy.spawn("google-chrome-stable")),
        Key([], 'd', lazy.spawn("firefox")),
        Key([], 'n', lazy.spawn("google-chrome-stable --incognito")),
    ]),

    # KEYS END!   
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", ]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "", "",]
group_labels = ["WEB", "DEV", "TER", "CHAT",
                "Meld", "Video", "Vb", "Files", "Mail", ]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall",
                 "monadtall", "monadtall", "monadtall", "monadtall", "treetab", ]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(
            i.name), lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin": 10,
            "border_width": 2,
            "border_focus": "#ff00ff",
            "border_normal": "#f4c2c2"
            }


layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=16, border_width=2,
                     border_focus="#ff00ff", border_normal="#f4c2c2"),
    layout.MonadWide(margin=16, border_width=2,
                     border_focus="#ff00ff", border_normal="#f4c2c2"),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(**layout_theme),
    # layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color='#141414',
        active_bg='#0000ff',
        inactive_bg='#1e90ff',
        padding_y=5,
        section_top=10,
        panel_width=280),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme)
]

# COLORS FOR THE BAR


def init_colors():
    return [["#2F343F", "#2F343F"],  # color 0
            ["#2F343F", "#2F343F"],  # color 1
            ["#c0c5ce", "#c0c5ce"],  # color 2
            ["#e75480", "#e75480"],  # color 3
            ["#f4c2c2", "#f4c2c2"],  # color 4
            ["#ffffff", "#ffffff"],  # color 5
            ["#ff0000", "#ff0000"],  # color 6
            ["#62FF00", "#62FF00"],  # color 7
            ["#000000", "#000000"],  # color 8
            ["#c40234", "#c40234"],  # color 9
            ["#6790eb", "#6790eb"],  # color 10
            ["#ff00ff", "#ff00ff"],  # 11
            ["#4c566a", "#4c566a"],  # 12
            ["#282c34", "#282c34"],  # 13
            ["#212121", "#212121"],  # 14
            ["#98c379", "#98c379"],  # 15
            ["#b48ead", "#b48ead"],  # 16
            ["#abb2bf", "#abb2bf"],  # color 17
            ["#81a1c1", "#81a1c1"],  # 18
            ["#56b6c2", "#56b6c2"],  # 19
            ["#c678dd", "#c678dd"],  # 20
            ["#e06c75", "#e06c75"],  # 21
            ["#fb9f7f", "#fb9f7f"],  # 22
            ["#ffd47e", "#ffd47e"]]  # 23


colors = init_colors()


def base(fg='text', bg='dark'):
    # return {'foreground': ["#ffffff", "#ffffff"],'background': ["#000000", "#000000"]}
    return {'foreground': colors[14], 'background': colors[1]}


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(
        font='Ubuntu, Mono Nerd Font',
        fontsize=14,
        padding=4,
        background=colors[1]
    )


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

        widget.Sep(
            linewidth=1,
            padding=10,
            foreground=colors[1],

        ),              #
        widget.Image(
            filename="~/.config/qtile/icons/garuda-red.png",
            iconsize=10,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('jgmenu_run')}
        ),
        widget.GroupBox(
            **base(bg=colors[1]),
            margin_y=3,
            padding_x=5,
            borderwidth=3,
            active=colors[5],
            highlight_color=colors[1],
            inactive=colors[6],
            rounded=True,
            highlight_method='line',
            urgent_alert_method='line',
            urgent_border=colors[6],
            this_current_screen_border=colors[6],
            this_screen_border=colors[6],
            other_current_screen_border=colors[6],
            other_screen_border=colors[6],
            disable_drag=True
        ),
        widget.Sep(linewidth=3),
        widget.TaskList(
            highlight_method="block",
            icon_size=0,
            max_title_width=200,
            rounded=False,
            padding=1,
            margin=1,
            padding_x=5,
            
            # border=colors[6],
            border=colors[6],
            background=colors[0],
            foreground=colors[5],
            
            txt_floating='🗗',
            txt_minimized='>_ ',

            borderwidth=1,
        ),

        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=1,
        ),

        widget.CurrentLayout(),

        # Hardware preformence
        # widget.Net(
        #     # Here enter your network name
        #     # interface=["wlo1"],
        #     format='{down} ↓↑ {up}',
        #     background=colors[10],
        #     foreground=colors[13],
        #     padding=0,
        # ),
        widget.Sep(linewidth=3),
        widget.NetGraph(
            # bandwidth_type="down",
            type="linefill",
            graph_color="ff0000.3",
            fill_color="ff0000",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,
        ),
        widget.NetGraph(
            bandwidth_type="up",
            type="linefill",
            graph_color="0098ff.3",
            fill_color="0088ff",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,
        ),
        # widget.CPU(
        #     update_interval=1,
        #     background=colors[10],
        #     foreground=colors[13],
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        # ),
        widget.Sep(linewidth=3),
        # widget.Sep(),
        widget.CPUGraph(
            type="linefill",
            graph_color="#00ffee",
            fill_color="#00ffee",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,  
        ),
        widget.MemoryGraph(
            type="linefill",
            graph_color="#eeff00",
            fill_color="#eeff00",
            border_width=0,
            line_width=3,
            samples=15,
            width=50,  
        ),
        # widget.Memory(
        #     format='{MemUsed: .0f}/{MemTotal: .0f}G',
        #     update_interval=1,
        #     measure_mem='G',
        #     background=colors[10],
        #     foreground=colors[13],
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        # ),
        widget.Sep(linewidth=3),
        # widget.Sep(),
        widget.Clock(
            format="%Y-%m-%d %H:%M"
        ),

        widget.BatteryIcon(
            # background=colors[14],
            
            theme_path="/home/bardia/.config/qtile/icons/battery_icons_horiz_2"
        ),
        widget.Battery(
            # background=colors[14],
            update_interval=15,
            format="{percent:2.0%} {hour:d}:{min:02d} | {watt}W"
        ),
        # widget.CapsNumLockIndicator(),
        widget.Chord(),
        widget.Systray(
            icon_size=20,
            padding=4,
            # margin_y=1,
        ),

    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.85, background="000000")),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.85, background="000000"))]


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["pcmanfm", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "pcmanfm", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(title='branchdialog'),
    Match(title='Open File'),
    Match(title='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='Lxpolkit'),
    Match(wm_class='yad'),
    Match(wm_class='Yad'),
    Match(wm_class='Cairo-dock'),
    Match(wm_class='cairo-dock'),


],  fullscreen_border_width=0, border_width=0)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"