#!/bin/sh

picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed


/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
nm-applet &
diodon &
volumeicon &
numlockx &
#feh --bg-scale ~/Pictures/od_debain.png  &
/usr/bin/syncthing serve --no-browser --logfile=default &
#picom &
blueman-applet &
xfce4-power-manager --daemon &
