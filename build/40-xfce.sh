echo "=============== XFCE / Xfce (1) ==============="
yay -S xfce4-settings --noconfirm
clear

echo "=============== XFCE / Compositor (1) ==============="
yay -S picom --noconfirm
clear

echo "=============== XFCE / Applauncher (3) ==============="
yay -S dmenu rofi rofi-calc --noconfirm
clear

echo "=============== XFCE / Desktop (2) ==============="
yay -S lxappearance dunst-git --noconfirm
clear

echo "=============== XFCE / Dm / Xorg! (2) ==============="
yay -S xorg xorg-xinit-git --noconfirm
clear

echo "=============== XFCE / Dm / Lightdm (4) ==============="
yay -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lightdm-webkit2-greeter --noconfirm
clear

echo "=============== XFCE / Themes / Icons! (2) ==============="
yay -S tela-icon-theme-git flatery-icon-theme-git --noconfirm
clear

echo "=============== XFCE / Themes / Cursors! (1) ==============="
yay -S capitaine-cursors --noconfirm
clear

echo "=============== XFCE / Themes / Colors! (4) ==============="
yay -S chicago95-gtk-theme-git gruvbox-material-gtk-theme-git yaru-gtk-theme materia-gtk-theme --noconfirm
clear

echo "=============== XFCE / Wm (1) ==============="
yay -S wmctrl --noconfirm
clear

echo "=============== XFCE / I3 (3) ==============="
yay -S i3 autotiling perl-anyevent-i3 --noconfirm
clear

echo "=============== XFCE / I3 / Lock (1) ==============="
yay -S i3lock --noconfirm
clear

echo "=============== XFCE / I3 / Bar (3) ==============="
yay -S i3blocks py3status polybar --noconfirm
clear

echo "=============== XFCE / Xmonad (4) ==============="
yay -S xmonad xmonad-contrib xmonad-utils xmonad-log --noconfirm
clear

echo "=============== XFCE / Xmonad / Haskell (1) ==============="
yay -S haskell-dbus --noconfirm
clear

echo "=============== XFCE / Xmonad / Bar (1) ==============="
yay -S xmobar --noconfirm
clear
