apps = {
    "apps/arch!":           ["paru", "ntp"],
    "apps/email!":          ["mailspring"],
    "apps/password!":       ["bitwarden-bin"],
    "apps/torrent!":        ["qbittorrent", "stremio"],
    "apps/browsers!":       ["chromium", "tor-browser", "firefox-nightly"],
    "apps/communication!":  ["discord_arch_electron", "zoom", "whatsapp-nativefier"],

    "config/screen!":       ["redshift"],
    "config/bluetooth!":    ["bluez", "bluez-libs", "bluez-utils", "blueberry"],
    "config/security!":     ["gnome-keyring"],

    "media/image!":         ["krita"],
    "media/video!":         ["vlc", "obs-studio"],

    "hardware/boot!":       ["os-prober", "grub-customizer", "woeusb"],
    "hardware/cpu!":        ["cpu-x-git", "s-tui", "stress"],
    "hardware/gpu!":        ["gwe"],
    "hardware/hd!":         ["gparted-git", "gsmartcontrol", "agedu", "ncdu"],

    "driver/open!":         ["xf86-video-nouveau", "mesa", "mesa-demos", "lib32-mesa"],
    "driver/nvidia!":       ["nvidia-390xx",
                             "nvidia-390xx-utils",
                             "lib32-nvidia-390xx-utils",
                             "nvidia-390xx-settings"],

    "terminal!":            ["xclip", "xsel", "youtube-dl", "tldr"],
    "terminal/fun!":        ["cava", "cbonsai", "lolcat", "hollywood"],
    "terminal/wm!":         ["tmux"],
    "terminal/filemanager!":["lf", "ranger", "w3m"],
    "terminal/zsh!":        ["zsh", "oh-my-zsh-git"],
    "terminal/zsh/config!": ["antigen-git", "spaceship-prompt-git"],
    "terminal/ui!":         ["lazygit-bin", "lazydocker-bin"],
    "terminal/ui/activity!":["gotop-bin", "htop"],
    "terminal/ui/sysinfo!": ["neofetch", "inxi"],

    "spotify!":             ["spotify-snap", "zenity", "ffmpeg-compat-57"],
    "spotify/spicetify":    ["spicetify-cli", "spicetify-themes-git"],

    "fonts/nerd!":          ["nerd-fonts-complete"],
    "fonts/misc":           ["awesome-terminal-fonts"],
    "fonts/ttf":            ["ttf-fira-code",
                             "ttf-ibm-plex-mono-git",
                             "ttf-liberation",
                             "ttf-roboto", "ttf-dejavu",
                             "ttf-droid",
                             "ttf-inconsolata",
                             "ttf-liberation",
                             "ttf-unifont",
                             "ttf-ms-fonts",
                             "ttf-liberation",
                             "ttf-font-icons"],
}

development = {
    "apps/cli!":            ["vsce", "exercism", "wakatime"],
    "apps/api!":            ["insomnia-bin", "postman-bin"],
    "apps/vm!":             ["docker", "virtualbox-ext-oracle"],

    "config/network!":      ["openssh"],
    "config/android!":      ["android-sdk", "android-tools", "kdeconnect"],
    "config/archiso!":      ["archiso-git", "qemu", "edk2-ovmf"],

    "editors!":             ["visual-studio-code-insiders-bin", "intellij-idea-community-edition", "neovim"],
    "editors/emacs!":       ["emacs", "fd", "ripgrep"],

    "lang/js":              ["nvm-git", "yarn"],
    "lang/php":             ["apache", "mysql", "php", "php-apache", "phpmyadmin"],
    "lang/java":            ["jdk", "glassfish5", "processing"],
    "lang/json":            ["jq"],
    "lang/shell":           ["shellcheck"],
    "lang/ocaml":           ["opam"],
    "lang/python":          ["python", "autopep8"],
    "lang/elixir":          ["elixir", "inotify-tools"],
    "lang/haskell":         ["ghc", "cabal-install-bin", "stack"],
    "lang/mark":            ["pandoc-bin"],

    "db/postgres":          ["postgresql", "pgadmin4"]

}


# -------------------------------------------------------------------------------------- #


plasma = {
    "kvantum!":             ["kvantum-qt5-git"],
    "kvantum/theme":        ["kvantum-theme-layan-git"],

    "desktop!":             ["plank", "superpaper"],
    "terminal!":            ["konsole", "yakuake"],
    "packfiles":            ["ark"],
    "filemanager!":         ["dolphin", "dolphin-plugins"],

    "media/image!":         ["gwenview"],
    "media/docs!":          ["okular"]
}

xfce = {
    "xfce":                 ["xfce4-settings"],
    "compositor!":          ["picom"],
    "menu!":                ["dmenu", "rofi", "rofi-calc"],

    "desktop!":             ["nitrogen", "lxappearance", "dunst-git"],
    "terminal!":            ["kitty", "alacritty-git", "xcompmgr"],
    "packfiles!":           ["xarchiver", "rar", "unrar", "zip", "unzip", "p7zip"],

    "filemanager!":         ["thunar", "thunar-archive-plugin", "thunar-volman"],
    "filemanager/tumbler!": ["tumbler", "ffmpegthumbnailer"],

    "filesystem!":          ["sshfs", "ntfs-3g"],
    "filesystem/mtp":       ["mtpfs", "jmtpfs"],
    "filesystem/gvfs":      ["gvfs", "gvfs-mtp", "gvfs-gphoto2"],

    "media/image!":         ["feh", "imagemagick", "flameshot-git", "gcolor2"],
    "media/video!":         ["mplayer"],
    "media/docs!":          ["evince"],
    "media/docs/zathura!":  ["zathura", "zathura-pdf-poppler", "zathura-djvu", "zathura-ps"],

    "audio/alsa!":          ["alsa-firmware", "alsa-lib", "alsa-plugins", "alsa-utils"],
    "audio/icon":           ["volumeicon"],
    "audio/cli!":           ["playerctl"],
    "audio/synthesis":      ["festival", "festival-us"],
    "audio/pulseaudio":     ["pulseaudio",
                             "pulseaudio-alsa",
                             "pulseeffects-legacy",
                             "pavucontrol"],

    "dm/xorg":              ["xorg", "xorg-xinit-git"],
    "dm/lightdm!":          ["lightdm",
                             "lightdm-gtk-greeter",
                             "lightdm-gtk-greeter-settings",
                             "lightdm-webkit2-greeter"],

    "themes/icons":         ["tela-icon-theme-git", "flatery-icon-theme-git"],
    "themes/cursors":       ["capitaine-cursors"],
    "themes/colors":        ["ant-dracula-gtk-theme",
                             "chicago95-gtk-theme-git",
                             "gruvbox-material-gtk-theme-git",
                             "yaru-gtk-theme"],
}


################################################################


i3 = {
    "i3!":                  ["i3-gaps", "autotiling-git", "perl-anyevent-i3"],
    "lock!":                ["i3lock"],
    "bar!":                 ["i3blocks", "py3status", "polybar"],
}


xmonad = {
    "xmonad!":              ["xmonad", "xmonad-contrib", "xmonad-utils", "xmonad-log"],
    "haskell!":             ["haskell-dbus"],
    "bar!":                 ["xmobar"],
}
