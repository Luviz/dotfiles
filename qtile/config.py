###############################################################
# >     __                _      <> QTile config              <#
# >    / /   __  ___   __(_)___  <> Bardia Jedi               <#
# >   / /   / / / / | / / /_  /  <> 2021                      <#
# >  / /___/ /_/ /| |/ / / / /_  <>                           <#
# > /_____/\__,_/ |___/_/ /___/  <> https://github.com/luviz  <#
# >                              <>                           <#
###############################################################

import os
import subprocess
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Drag, Group, Key, KeyChord, Match, Screen
from libqtile.command import lazy
from resize import Resize
import re

# from libqtile.widget import BatteryIcon, BatteryState, Battery

# from libqtile.widget import Spacer

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")

## Core color pallet based on ink_in_water
core_color_pallet = {
    "red": "#D62B24",
    "darkBlue": "#012F4A",
    "rose": "#A43E66",
    "blue": "#07467B",
    "brown": "#783934",
}

vscode = "code-insiders"  # "code"

wallpapares_path = "/usr/share/wallpapers/bardia"
bar_icon_path = "/usr/share/icons/bardia/archlinux-icon.svg"

myTerm = "alacritty"  # My terminal of choice


class Commands:
    lock_screen = f"i3lock -efi {wallpapares_path}/lockscreen/ink_in_water.png"
    d_menu = "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'"
    rofi = f"bash {home}/.config/qtile/scripts/rofi.sh"
    task_manager = f"{myTerm} -e btop"
    brightness = lambda v: f"xbacklight -inc {v} -step 20"
    picom = f"{home}/.config/qtile/scripts/picom-toggle.sh"
    file_manager = "pcmanfm"
    audio_manager = "pavucontrol"
    vol_mute = "pamixer --toggle-mute"
    vol_inc = lambda v: f"pamixer --increase {v}"
    vol_dec = lambda v: f"pamixer --decrease {v}"
    toggle_keyboard = f"{home}/.config/qtile/scripts/chlay.sh"


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


keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "v", lazy.spawn(Commands.audio_manager)),
    Key([mod], "e", lazy.spawn(Commands.file_manager)),
    Key([mod], "o", lazy.spawn(Commands.lock_screen)),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn(myTerm)),
    Key([mod], "x", lazy.shutdown()),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn(Commands.file_manager)),
    Key([mod, "shift"], "d", lazy.spawn(Commands.rofi)),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    # SUPER + ALT
    Key([mod, "mod1"], "space", lazy.spawn(Commands.toggle_keyboard)),
    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "o", lazy.spawn(Commands.picom)),
    Key(["mod1", "control"], "t", lazy.spawn(myTerm)),
    # ALT + ... KEYS
    Key(["mod1", "control"], "p", lazy.spawn("nwggrid -p -o 0.4")),
    # SCREENSHOTS
    Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures/flameshot")),
    Key(["control"], "Print", lazy.spawn("flameshot gui")),
    # MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn(Commands.brightness(10))),
    Key([], "XF86MonBrightnessDown", lazy.spawn(Commands.brightness(-10))),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn(Commands.vol_mute)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(Commands.vol_dec(5))),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(Commands.vol_inc(5))),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "m", lazy.layout.maximize()),
    KeyChord(
        [mod],
        "p",
        [
            Key([], "p", lazy.group.setlayout("max")),
            # Key([],"l", lazy.group.setlayout("treetab")), ## dose not work - side panel wont show
            Key([], "o", lazy.group.setlayout("monadtall")),
            Key([], "i", lazy.group.setlayout("monadwide")),
        ],
        name="change layout (p, o, i)",
    ),
    KeyChord(
        [mod],
        "y",
        [
            Key([], "l", lazy.group.setlayout("max")),
            Key([], "o", lazy.group.setlayout("monadtall")),
            Key([], "Up", *Resize.RS_UP()),
            Key([], "Down", *Resize.RS_DOWN()),
            Key([], "Left", *Resize.RS_LEFT()),
            Key([], "Right", *Resize.RS_RIGHT()),
        ],
        name="win size (arrow keys)",
        mode=True,
    ),
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
    Key([mod, "control"], "l", *Resize.RS_RIGHT()),
    Key([mod, "control"], "Right", *Resize.RS_RIGHT()),
    Key([mod, "control"], "h", *Resize.RS_LEFT()),
    Key([mod, "control"], "Left", *Resize.RS_LEFT()),
    Key([mod, "control"], "k", *Resize.RS_UP()),
    Key([mod, "control"], "Up", *Resize.RS_UP()),
    Key([mod, "control"], "j", *Resize.RS_DOWN()),
    Key([mod, "control"], "Down", *Resize.RS_DOWN()),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # Treetab controls
    Key(
        [mod, "control"],
        "k",
        lazy.layout.section_up(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.section_down(),
        desc="Move down a section in treetab",
    ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    # Key([mod],  "z", lazy.screen.toggle_group()),
    Key([mod], "Tab", lazy.screen.toggle_group()),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
    # LUNCH APPS
    ## DEV - lunch Code
    KeyChord(
        [mod],
        "d",
        [
            Key([], "p", lazy.spawn(f"{vscode} /home/bardia/.config/")),
            Key([], "d", lazy.spawn(f"{vscode} /home/bardia/mynotes/")),
            Key([], "n", lazy.spawn(f"{vscode} -n")),
        ],
        name="code [p: config | d: notes]"
    ),
    ## Quick App
    KeyChord(
        [mod],
        "a",
        [
            Key([], "a", lazy.spawn("google-chrome-stable")),
            Key([], "d", lazy.spawn("firefox")),
            Key([], "n", lazy.spawn("google-chrome-stable --incognito")),
        ],
        name="browser [a: chrome | d: ff | n: chrome incognito]"
    ),
    # KEYS END!
]

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["WEB", "DEV", "TER", "CHAT", "5", "6", "7", "8", "Mail", "TUX"]

group_layouts = [
    "max",
    "monadtall",
    "monadtall",
    "max",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "treetab",
    "max",
]

groups = [
    Group(name=n, label=l, layout=ly)
    for n, l, ly in zip(group_names, group_labels, group_layouts)
]

## Setup group configs
for group in groups:
    if group.label == "CHAT":
        group.matches = [
            Match(wm_class=re.compile(r"^(microsoft teams - preview|slack)$"))
        ]

    if group.label == "TUX":
        group.matches = [Match(wm_class=re.compile(r"^(tuxedo-control-center)$"))]

    if group.label == "Mail":
        group.matches = [Match(wm_class=re.compile(r"^(prospect mail)$"))]

    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], group.name, lazy.group[group.name].toscreen(toggle=True)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name),
                lazy.group[group.name].toscreen(),
            ),
        ]
    )


color_layout_theme = {
    "border_focus": core_color_pallet["blue"],
    "border_normal": core_color_pallet["darkBlue"],
}

common_layout_theme = {"margin": 10, "border_width": 2, **color_layout_theme}


layouts = [
    layout.MonadTall(margin=16, border_width=2, **color_layout_theme),
    layout.MonadWide(margin=16, border_width=2, **color_layout_theme),
    layout.Floating(**common_layout_theme),
    layout.Max(**common_layout_theme),
    layout.TreeTab(
        sections=["Tabs"],
        bg_color=core_color_pallet["darkBlue"],
        active_bg=core_color_pallet["red"],
        inactive_bg=core_color_pallet["blue"],
        padding_y=5,
        section_top=10,
        panel_width=280,
    ),
]

color_pallet = {
    "bar-bg": core_color_pallet["darkBlue"],
    "bar-fg": "#ffffff",
    "active-bg": core_color_pallet["red"],
    "active-fg": "#ff0000",
    "white": "#d8d8d8",
    "test": "#00ff00",
}

base = {"foreground": color_pallet["bar-fg"], "background": color_pallet["bar-bg"]}


# WIDGETS FOR THE BAR

widget_defaults = dict(
    font="Ubuntu, Mono Nerd Font",
    fontsize=14,
    padding=4,
    background=color_pallet["bar-bg"],
)

sep = widget.Sep(linewidth=3)


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=1,
            padding=14,
            foreground=color_pallet["bar-bg"],
        ),
        widget.Image(
            filename=bar_icon_path,
            iconsize=10,
        ),
        widget.GroupBox(
            margin_y=3,
            padding_x=5,
            borderwidth=3,
            active=color_pallet["white"],
            highlight_color=color_pallet["bar-bg"],
            inactive=color_pallet["active-fg"],
            highlight_method="line",
            urgent_alert_method="line",
            urgent_border=color_pallet["active-bg"],
            this_current_screen_border=color_pallet["active-bg"],
            this_screen_border=color_pallet["active-bg"],
            other_current_screen_border=color_pallet["active-bg"],
            other_screen_border=color_pallet["active-bg"],
            disable_drag=True,
        ),
        sep,
        widget.TaskList(
            highlight_method="block",
            icon_size=0,
            max_title_width=300,
            rounded=False,
            padding=1,
            margin=1,
            padding_x=5,
            border=color_pallet["active-bg"],
            background=color_pallet["bar-bg"],
            foreground=color_pallet["white"],
            txt_floating="🗗",
            txt_minimized=">_ ",
            borderwidth=1,
        ),
        # Hardware preformence
        widget.Chord(),
        sep,
        widget.NetGraph(
            # bandwidth_type="down",
            **widget_defaults,
            type="linefill",
            graph_color="ff0000",
            fill_color="ff0000",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,
            mouse_callbacks={"Button1": lambda: qtile.spawn(Commands.task_manager)},
        ),
        widget.NetGraph(
            bandwidth_type="up",
            type="linefill",
            graph_color="0098ff",
            fill_color="0088ff",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,
            mouse_callbacks={"Button1": lambda: qtile.spawn(Commands.task_manager)},
        ),
        sep,
        widget.CPUGraph(
            type="linefill",
            graph_color="#00ffee",
            fill_color="#00ffee",
            border_width=0,
            line_width=3,
            samples=25,
            width=50,
            mouse_callbacks={"Button1": lambda: qtile.spawn(Commands.task_manager)},
        ),
        widget.MemoryGraph(
            type="linefill",
            graph_color="#eeff00",
            fill_color="#eeff00",
            border_width=0,
            line_width=3,
            samples=15,
            width=50,
            mouse_callbacks={"Button1": lambda: qtile.spawn(Commands.task_manager)},
        ),
        sep,
        widget.Clock(format="%Y-%m-%d %H:%M"),
        widget.Sep(linewidth=3, padding_x=4),
        widget.Systray(icon_size=16),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=15,
        ),
    ]
    return widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=20,
                opacity=0.85,
                background="000000",
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(),
                size=20,
                opacity=0.85,
                background="000000",
            )
        ),
    ]


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(title="branchdialog"),
        Match(title="Open File"),
        Match(title="pinentry"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="Lxpolkit"),
        Match(wm_class="yad"),
        Match(wm_class="Yad"),
        Match(wm_class="Cairo-dock"),
        Match(wm_class="cairo-dock"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)

auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
