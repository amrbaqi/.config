# My Config of Qtile WM on Linux Mint   
# Using Rofi - 
# amr@amr 

from libqtile import bar, layout, widget, qtile 
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

mod = "mod4"
terminal = "xfce4-terminal"

keys = [
    
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
   
    # Switch between windows

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "v", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),  
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Toggle miniimize"),  
    Key([mod, "shift"], "space", lazy.widget['keyboardlayout'].next_keyboard()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"],"Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes  

    # Toggle between different layouts as defined below

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    
    # ROFi KEYBINDING & Launch apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Launch Rofi"),
    Key([mod], "t", lazy.spawn("rofi -show drun"), desc="spawn rofi"),
    Key([mod], "a", lazy.spawn("rofi -show window"), desc="spawn rofi"),
    Key([mod], "p", lazy.spawncmd(),desc="Run a command using a prompt widget"),    

    Key([mod], "b", lazy.spawn("brave-browser-stable"), desc="spawn brave-browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="spawn Thunar"),
    Key([mod], "o",lazy.group["9"].toscreen(), lazy.spawn("/home/amr/Appimage/Obsidian-1.3.5.AppImage"), desc="spawn Obsidian"),
    
    # Brightness controls
    
    #Key([],"XF86MonBrightnessUp",lazy.spawn("brightnessctl set +5%"),desc="Raise screen brightness" ),
    #Key([],"XF86MonBrightnessDown",lazy.spawn("brightnessctl set 5%-"),desc="Lower screen brightness"),
   
   
]


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod],i.name,lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name),),
            
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True),desc="Switch to & move focused window to group {}".format(i.name),),
            
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=3),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
   # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(margin=6, border_focus='#d75f5f'border_normal='#2c5380'),
   # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
     layout.TreeTab(vspace=4,panel_width=120,),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    #  layout.Floating(),
]



widget_defaults = dict(
    font="Cantarell Bold",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
	wallpaper='~/Pictures/od_bash.png',
	wallpaper_mode='fill',
        top=bar.Bar(
            [	
		            widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/qtile.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.spawn("rofi -show drun")}),
                widget.CurrentLayout(highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#2f343f"),
                widget.Sep(padding=2, linewidth=0, background="#2f343f"), 
                widget.GroupBox(highlight_method='block',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#585F73",
                                background="#2f343f",
                                padding = 3,
                                disable_drag= True,  rounded=True,
                                ),
								widget.TextBox(
                       text ='',
                       padding = -1,
                       fontsize = 40,
                       foreground='#2f343f' , 
                       ), 
                widget.Spacer(length=5),              
                widget.Prompt(foreground='#99c0de'),
                widget.Spacer(length=5),

                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                          ),
               widget.TextBox("  Nada    | ", name="default", foreground="#55CC80"),

		           widget.KeyboardLayout(configured_keyboards=["us", "ara"],
							   font="Noto Sans Bold" ,
								 fontsize=12, foreground="#55CC80",),	
								  widget.Spacer(length=3),
                widget.TextBox("",fontsize = 50, padding =-7,background="#404552",foreground="#2F343F",),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(background="#2F343F",
                    padding=6,
                    icon_size=20),
                widget.Sep(padding=0, background="#2F343F",foreground="#2F343F",linewidth=5), 
                widget.TextBox("",fontsize = 50, padding = -7,foreground="#404552",background="#2F343F"),
                widget.Battery(battery="BAT1", format = '   {percent:2.0%} ', charge_char='AC',
                    discharge_char='DC' ,
                    update_interval=1 ,font="Hack Nerd Font Regular"
                  ),
                #widget.TextBox(text = "", padding =3 ,fontsize = 20,mouse_callbacks={'Button1': lambda: qtile.spawn("gnome-calendar")}),          

                 widget.TextBox(text = "", padding =2 ,fontsize = 20,mouse_callbacks={'Button1': lambda: qtile.spawn("thunar")}), 
                 widget.Sep(padding=2, linewidth=0, background="#404552"), 
     
                widget.Image(filename='/home/amr/Appimage/obsidian-icon.png',padding =10 , margin=2, mouse_callbacks={'Button1': lambda: qtile.spawn("/home/amr/Appimage/Obsidian-1.3.5.AppImage")}),
                widget.Sep(padding=2, linewidth=0, background="#404552"), 
                widget.TextBox("",fontsize = 40, padding =-3 ,foreground="#2f343f"),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background="#2f343f"),
                widget.QuickExit(background="#2f343f"),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
			background="#404552"  # background color
        ),
    ),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/amr/.config/qtile/autostart.sh')
    subprocess.call([home])
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = [
]  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='confirm'),
        Match(wm_class='feh'),
        Match(wm_class='audacious'), 
        Match(wm_class='gnome-calculator'), 
	Match(wm_class='gthumb'),
        Match(wm_class='video-downloader'), 
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
