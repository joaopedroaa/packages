#!/bin/bash

echo "======================================================="
echo "==       Iniciando a instalação de todos os pacotes      =="
echo "======================================================="
clear

# --- Conteúdo de 10-system.sh ---

echo "=============== System / System (3) ==============="
yay -S tree words stow --noconfirm
clear

echo "=============== System / Book (2) ==============="
yay -S calibre fbreader-qt5 --noconfirm
clear

echo "=============== System / Color (1) ==============="
yay -S python-pywal --noconfirm
clear

echo "=============== System / Wine (3) ==============="
yay -S wine winetricks lutris --noconfirm
clear

echo "=============== System / Game (2) ==============="
yay -S tlauncher-org mcaselector --noconfirm
clear

echo "=============== System / Clock (1) ==============="
yay -S ntp --noconfirm
clear

echo "=============== System / Keyboard  (1) ==============="
yay -S xkeycaps --noconfirm
clear

echo "=============== System / Cleaning (1) ==============="
yay -S bleachbit --noconfirm
clear

echo "=============== System / Socialnetwork (1) ==============="
yay -S sherlock-git --noconfirm
clear

echo "=============== System / Screen (2) ==============="
yay -S redshift caffeine-ng-git --noconfirm
clear

echo "=============== System / Bluetooth (4) ==============="
yay -S bluez bluez-libs bluez-utils blueberry --noconfirm
clear

echo "=============== System / Security (1) ==============="
yay -S gnome-keyring --noconfirm
clear

echo "=============== System / Fontviewers (1) ==============="
yay -S font-manager --noconfirm
clear

echo "=============== System / Net (1) ==============="
yay -S httpie --noconfirm
clear

echo "=============== System / Filesharing / Ftp (1) ==============="
yay -S openssh --noconfirm
clear

echo "=============== System / Apps / Arch (1) ==============="
yay -S paru --noconfirm
clear

echo "=============== System / Apps / Email (1) ==============="
yay -S mailspring --noconfirm
clear

echo "=============== System / Apps / Password (1) ==============="
yay -S bitwarden --noconfirm
clear

echo "=============== System / Apps / Network (1) ==============="
yay -S ipscan --noconfirm
clear

echo "=============== System / Apps / Network / Nmap (2) ==============="
yay -S nmap zenmap --noconfirm
clear

echo "=============== System / Apps / Vulnerability (1) ==============="
yay -S lynis --noconfirm
clear

echo "=============== System / Apps / Hamachi (2) ==============="
yay -S logmein-hamachi haguichi --noconfirm
clear

echo "=============== System / Apps / Torrent (2) ==============="
yay -S qbittorrent stremio --noconfirm
clear

echo "=============== System / Apps / Browsers (3) ==============="
yay -S firefox chromium i2p-bin --noconfirm
clear

echo "=============== System / Apps / Messaging (3) ==============="
yay -S element-desktop zoom whatsapp-nativefier --noconfirm
clear

echo "=============== System / Apps / Messaging / Discord (2) ==============="
yay -S discord_arch_electron betterdiscordctl-git --noconfirm
clear

echo "=============== System / Apps / Spotify (3) ==============="
yay -S spotify zenity ffmpeg-compat-57 --noconfirm
clear

echo "=============== System / Apps / Spotify / Spicetify (2) ==============="
yay -S spicetify-cli spicetify-themes-git --noconfirm
clear

echo "=============== System / Driver (1) ==============="
yay -S mesa-demos --noconfirm
clear

echo "=============== System / Driver / Nvidia (4) ==============="
yay -S nvidia nvidia-utils lib32-nvidia-utils nvidia-settings --noconfirm
clear

echo "=============== System / Driver / Nvidia-games (4) ==============="
yay -S dxvk-bin nvidia-dkms vulkan-icd-loader lib32-vulkan-icd-loader --noconfirm
clear

echo "=============== System / Hardware / Boot (2) ==============="
yay -S os-prober grub-customizer --noconfirm
clear

echo "=============== System / Hardware / Boot / Create (2) ==============="
yay -S etcher-bin woeusb --noconfirm
clear

echo "=============== System / Hardware / Cpu (3) ==============="
yay -S cpu-x-git s-tui stress --noconfirm
clear

echo "=============== System / Hardware / Gpu (1) ==============="
yay -S gwe --noconfirm
clear

echo "=============== System / Hardware / Hd (3) ==============="
yay -S gparted-git gsmartcontrol gnome-disk-utility --noconfirm
clear

echo "=============== System / Hardware / Hd / Size (4) ==============="
yay -S ncdu dust agedu duf --noconfirm
clear

echo "=============== System / Audio / Cli (1) ==============="
yay -S playerctl --noconfirm
clear

echo "=============== System / Audio / Synthesis (2) ==============="
yay -S festival festival-us --noconfirm
clear

echo "=============== System / Audio / Alsa (4) ==============="
yay -S alsa-firmware alsa-lib alsa-plugins alsa-utils --noconfirm
clear

echo "=============== System / Audio / Pulseaudio (4) ==============="
yay -S pulseaudio pulseaudio-alsa pulseeffects-legacy pavucontrol --noconfirm
clear

echo "=============== System / Media / Image / Viewers (2) ==============="
yay -S feh gwenview --noconfirm
clear

echo "=============== System / Media / Image / Editors (2) ==============="
yay -S krita inkscape --noconfirm
clear

echo "=============== System / Media / Image / Wallsetter (2) ==============="
yay -S nitrogen imagemagick --noconfirm
clear

echo "=============== System / Media / Image / Screenshot (3) ==============="
yay -S flameshot-git gcolor2 scrot --noconfirm
clear

echo "=============== System / Media / Video / Players (3) ==============="
yay -S vlc mplayer obs-studio --noconfirm
clear

echo "=============== System / Media / Video / Edit (1) ==============="
yay -S video-trimmer --noconfirm
clear

echo "=============== System / Media / Documents (2) ==============="
yay -S evince okular --noconfirm
clear

echo "=============== System / Media / Documents / Zathura (4) ==============="
yay -S zathura zathura-pdf-poppler zathura-djvu zathura-ps --noconfirm
clear

echo "=============== System / Terminal / Emulators (5) ==============="
yay -S alacritty-git kitty xcompmgr konsole yakuake --noconfirm
clear

echo "=============== System / Terminal / Multiplexers (1) ==============="
yay -S tmux --noconfirm
clear

echo "=============== System / Terminal / Shell / Zsh (1) ==============="
yay -S zsh --noconfirm
clear

echo "=============== System / Terminal / Shell / Zsh / Config (2) ==============="
yay -S antigen-git lscolors-git --noconfirm
clear

echo "=============== System / Terminal / Commandline (4) ==============="
yay -S xclip xsel iftop lsd --noconfirm
clear

echo "=============== System / Terminal / Commandline / Net (1) ==============="
yay -S httpstat-go --noconfirm
clear

echo "=============== System / Terminal / Commandline / Color (2) ==============="
yay -S bat most --noconfirm
clear

echo "=============== System / Terminal / Commandline / Finder (3) ==============="
yay -S fd fzf the_silver_searcher --noconfirm
clear

echo "=============== System / Terminal / Commandline / Taskmanager (3) ==============="
yay -S gotop-bin htop tiptop-cli --noconfirm
clear

echo "=============== System / Terminal / Commandline / Sysinfo (4) ==============="
yay -S neofetch inxi tldr macchina-bin --noconfirm
clear

echo "=============== System / Terminal / Commandline / Lazy (2) ==============="
yay -S lazygit lazydocker --noconfirm
clear

echo "=============== System / Terminal / Commandline / Fun (4) ==============="
yay -S cava cbonsai lolcat hollywood --noconfirm
clear

echo "=============== System / Terminal / Commandline / Git (2) ==============="
yay -S git-open-git git-delta --noconfirm
clear

echo "=============== System / Terminal / Commandline / Time (1) ==============="
yay -S calcurse --noconfirm
clear

echo "=============== System / Terminal / Commandline / Hexviewer (1) ==============="
yay -S hexyl --noconfirm
clear

echo "=============== System / Terminal / Commandline / Images (1) ==============="
yay -S pacgraph --noconfirm
clear

echo "=============== System / Terminal / Commandline / Video (1) ==============="
yay -S youtube-dl --noconfirm
clear

echo "=============== System / File / Archivemanagers (2) ==============="
yay -S ark xarchiver --noconfirm
clear

echo "=============== System / File / Archivemanagers / Console (5) ==============="
yay -S rar unrar zip unzip p7zip --noconfirm
clear

echo "=============== System / Filesystem (2) ==============="
yay -S sshfs ntfs-3g --noconfirm
clear

echo "=============== System / Filesystem / Mtp (2) ==============="
yay -S mtpfs jmtpfs --noconfirm
clear

echo "=============== System / Filesystem / Gvfs (3) ==============="
yay -S gvfs gvfs-mtp gvfs-gphoto2 --noconfirm
clear

echo "=============== System / Filemanager / Console (3) ==============="
yay -S ranger nnn lf --noconfirm
clear

echo "=============== System / Filemanager / Console / Image (2) ==============="
yay -S w3m ueberzug --noconfirm
clear

echo "=============== System / Filemanager / Graph (1) ==============="
yay -S pcmanfm --noconfirm
clear

echo "=============== System / Filemanager / Graph / Dolphin (2) ==============="
yay -S dolphin dolphin-plugins --noconfirm
clear

echo "=============== System / Filemanager / Graph / Thunar (3) ==============="
yay -S thunar thunar-archive-plugin thunar-volman --noconfirm
clear

echo "=============== System / Filemanager / Graph / Thunar / Tumbler (2) ==============="
yay -S tumbler ffmpegthumbnailer --noconfirm
clear

echo "=============== System / Fonts / Editor (1) ==============="
yay -S gucharmap --noconfirm
clear

echo "=============== System / Fonts / Nerd (1) ==============="
yay -S nerd-fonts-complete --noconfirm
clear

echo "=============== System / Fonts / Misc! (1) ==============="
yay -S awesome-terminal-fonts --noconfirm
clear

echo "=============== System / Fonts / Ttc! (2) ==============="
yay -S ttc-iosevka ttc-iosevka-ss15 --noconfirm
clear

echo "=============== System / Fonts / Ttf! (12) ==============="
yay -S ttf-fira-code ttf-ibm-plex-mono-git ttf-liberation ttf-roboto ttf-dejavu ttf-droid ttf-inconsolata ttf-liberation ttf-unifont ttf-ms-fonts ttf-liberation ttf-font-icons --noconfirm
clear

echo "=============== System / Fonts / Emoji! (1) ==============="
yay -S noto-fonts-emoji --noconfirm
clear



# --- Conteúdo de 20-dev.sh ---

echo "=============== Dev / Apps / Cli (4) ==============="
yay -S vsce exercism wakatime ngrok --noconfirm
clear

echo "=============== Dev / Apps / Api (2) ==============="
yay -S insomnia-bin postman-bin --noconfirm
clear

echo "=============== Dev / Apps / Vm (1) ==============="
yay -S docker --noconfirm
clear

echo "=============== Dev / Apps / Virtualbox (2) ==============="
yay -S virtualbox virtualbox-host-dkms --noconfirm
clear

echo "=============== Dev / Config / Android (3) ==============="
yay -S android-sdk android-tools kdeconnect --noconfirm
clear

echo "=============== Dev / Config / Archiso (3) ==============="
yay -S archiso-git qemu edk2-ovmf --noconfirm
clear

echo "=============== Dev / Editors (3) ==============="
yay -S visual-studio-code-insiders-bin intellij-idea-community-edition neovim --noconfirm
clear

echo "=============== Dev / Editors / Emacs (2) ==============="
yay -S emacs ripgrep --noconfirm
clear

echo "=============== Dev / Lang / Js (2) ==============="
yay -S nvm-git yarn --noconfirm
clear

echo "=============== Dev / Lang / Php! (5) ==============="
yay -S apache mysql php php-apache phpmyadmin --noconfirm
clear

echo "=============== Dev / Lang / Java (3) ==============="
yay -S jdk glassfish5 processing --noconfirm
clear

echo "=============== Dev / Lang / Json (1) ==============="
yay -S jq --noconfirm
clear

echo "=============== Dev / Lang / Shell (1) ==============="
yay -S shellcheck --noconfirm
clear

echo "=============== Dev / Lang / Ocaml (1) ==============="
yay -S opam --noconfirm
clear

echo "=============== Dev / Lang / Python (2) ==============="
yay -S python autopep8 --noconfirm
clear

echo "=============== Dev / Lang / Elixir (2) ==============="
yay -S elixir inotify-tools --noconfirm
clear

echo "=============== Dev / Lang / Haskell (3) ==============="
yay -S ghc cabal-install-bin stack --noconfirm
clear

echo "=============== Dev / Lang / Lisp (1) ==============="
yay -S racket --noconfirm
clear

echo "=============== Dev / Lang / Mark (1) ==============="
yay -S pandoc-bin --noconfirm
clear

echo "=============== Dev / Db / Postgres (2) ==============="
yay -S postgresql pgadmin4 --noconfirm
clear



# --- Conteúdo de 30-plasma.sh ---

echo "=============== Plasma / Desktop (1) ==============="
yay -S superpaper --noconfirm
clear

echo "=============== Plasma / Desktop / Kvantum (1) ==============="
yay -S kvantum-qt5-git --noconfirm
clear

echo "=============== Plasma / Desktop / Kvantum / Theme (1) ==============="
yay -S kvantum-theme-layan-git --noconfirm
clear

echo "=============== Plasma / Desktop / Taskbars (1) ==============="
yay -S plank --noconfirm
clear



# --- Conteúdo de 40-xfce.sh ---

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
yay -S i3-gaps autotiling perl-anyevent-i3 --noconfirm
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



echo "======================================================="
echo "==          Instalação de todos os pacotes concluída!          =="
======================================================="