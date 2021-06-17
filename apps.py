system = {
    "clock":                    ["ntp"],
    "cleaning":                 ["bleachbit"],
    "screen":                   ["redshift"],
    "bluetooth":                ["bluez", "bluez-libs", "bluez-utils", "blueberry"],
    "security":                 ["gnome-keyring"],
    "filesharing/ftp":          ["openssh"],

    # -----------------------------------------------------------------------------------#
    #                               Application
    # -----------------------------------------------------------------------------------#
    "apps/arch":                ["paru"],
    "apps/email":               ["mailspring"],
    "apps/password":            ["bitwarden-bin"],
    "apps/torrent":             ["qbittorrent", "stremio"],
    "apps/browsers":            ["firefox-nightly", "chromium", "tor-browser"],

    "apps/instantMessaging":    ["discord_arch_electron", "zoom", "whatsapp-nativefier"],

    "apps/spotify":             ["spotify-snap", "zenity", "ffmpeg-compat-57"],
    "apps/spotify/spicetify":   ["spicetify-cli", "spicetify-themes-git"],

    # -----------------------------------------------------------------------------------#
    #                               Driver
    # -----------------------------------------------------------------------------------#
    "driver/open":              ["xf86-video-nouveau", "mesa", "mesa-demos", "lib32-mesa"],
    "driver/nvidia":            ["nvidia-390xx", "nvidia-390xx-utils",
                                 "lib32-nvidia-390xx-utils", "nvidia-390xx-settings"],


    # -----------------------------------------------------------------------------------#
    #                               Hardware
    # -----------------------------------------------------------------------------------#
    "hardware/boot":            ["os-prober", "grub-customizer", "woeusb"],
    "hardware/cpu":             ["cpu-x-git", "s-tui", "stress"],
    "hardware/gpu":             ["gwe"],
    "hardware/hd":              ["gparted-git", "gsmartcontrol", "agedu", "ncdu"],



    # -----------------------------------------------------------------------------------#
    #                               Audio
    # -----------------------------------------------------------------------------------#
    "audio/alsa":               ["alsa-firmware", "alsa-lib", "alsa-plugins", "alsa-utils"],
    "audio/icon":               ["volumeicon"],
    "audio/cli":                ["playerctl"],
    "audio/synthesis":          ["festival", "festival-us"],
    "audio/pulseaudio":         ["pulseaudio", "pulseaudio-alsa", "pulseeffects-legacy", "pavucontrol"],


    # -----------------------------------------------------------------------------------#
    #                               Media
    # -----------------------------------------------------------------------------------#
    "media/image/viewers":      ["feh", "gwenview"],
    "media/image/editors":      ["krita"],
    "media/image/wallsetter":   ["nitrogen", "imagemagick"],
    "media/image/screenshot":   ["flameshot-git", "gcolor2"],

    "media/video/players":      ["vlc", "mplayer", "obs-studio"],

    "media/documents":          ["evince", "okular"],
    "media/documents/zathura":  ["zathura",
                                 "zathura-pdf-poppler",
                                 "zathura-djvu",
                                 "zathura-ps"],


    # -----------------------------------------------------------------------------------#
    #                               Terminal
    # -----------------------------------------------------------------------------------#
    "terminal/emulators":                  ["alacritty-git", "kitty", "xcompmgr", "konsole", "yakuake"],
    "terminal/multiplexers":               ["tmux"],

    "terminal/shell/zsh":                  ["zsh", "oh-my-zsh-git"],
    "terminal/shell/zsh/config":           ["antigen-git", "spaceship-prompt-git"],

    "terminal/commandline":                ["xclip", "xsel", "tldr", "hexyl"],
    "terminal/commandline/images":         ["ueberzug", "pacgraph"],
    "terminal/commandline/video":          ["youtube-dl"],
    "terminal/commandline/finder":         ["fd", "fzf", "the_silver_searcher"],
    "terminal/commandline/taskmanager":    ["gotop-bin", "htop"],
    "terminal/commandline/sysinfo":        ["neofetch", "inxi"],
    "terminal/commandline/lazy":           ["lazygit-bin", "lazydocker-bin"],
    "terminal/commandline/fun":            ["cava", "cbonsai", "lolcat", "hollywood"],


    # -----------------------------------------------------------------------------------#
    #                               Files
    # -----------------------------------------------------------------------------------#
    "file/archivemanagers":                ["ark", "xarchiver"],
    "file/archivemanagers/console":        ["rar", "unrar", "zip", "unzip", "p7zip"],

    "file/filesystem":                     ["sshfs", "ntfs-3g"],
    "file/filesystem/mtp":                 ["mtpfs", "jmtpfs"],
    "file/filesystem/gvfs":                ["gvfs", "gvfs-mtp", "gvfs-gphoto2"],

    "file/filemanager/console":                    ["lf", "ranger", "w3m"],
    "file/filemanager/graphical":                  ["dolphin", "dolphin-plugins"],
    "file/filemanager/graphical/thunar":           ["thunar", "thunar-archive-plugin", "thunar-volman"],
    "file/filemanager/graphical/thunar/tumbler":   ["tumbler", "ffmpegthumbnailer"],


    # -----------------------------------------------------------------------------------#
    #                               Fonts
    # -----------------------------------------------------------------------------------#
    "fonts/nerd!":          ["nerd-fonts-complete"],
    "fonts/misc!":          ["awesome-terminal-fonts"],
    "fonts/ttf!":           ["ttf-fira-code",
                             "ttf-ibm-plex-mono-git",
                             "ttf-liberation",
                             "ttf-roboto",
                             "ttf-dejavu",
                             "ttf-droid",
                             "ttf-inconsolata",
                             "ttf-liberation",
                             "ttf-unifont",
                             "ttf-ms-fonts",
                             "ttf-liberation",
                             "ttf-font-icons"],

}

development = {
    "apps/cli":            ["vsce", "exercism", "wakatime"],
    "apps/api":            ["insomnia-bin", "postman-bin"],
    "apps/vm":             ["docker", "virtualbox-ext-oracle"],

    "config/android":      ["android-sdk", "android-tools", "kdeconnect"],
    "config/archiso":      ["archiso-git", "qemu", "edk2-ovmf"],

    # -----------------------------------------------------------------------------------#
    #                               Development environments
    # -----------------------------------------------------------------------------------#
    "editors":             ["visual-studio-code-insiders-bin",
                            "intellij-idea-community-edition",
                            "neovim"],
    "editors/emacs":       ["emacs", "ripgrep"],

    # -----------------------------------------------------------------------------------#
    #                               Lang
    # -----------------------------------------------------------------------------------#
    "lang/js":              ["nvm-git", "yarn"],
    "lang/php!":            ["apache", "mysql", "php", "php-apache", "phpmyadmin"],
    "lang/java":            ["jdk", "glassfish5", "processing"],
    "lang/json":            ["jq"],
    "lang/shell":           ["shellcheck"],
    "lang/ocaml":           ["opam"],
    "lang/python":          ["python", "autopep8"],
    "lang/elixir":          ["elixir", "inotify-tools"],
    "lang/haskell":         ["ghc", "cabal-install-bin", "stack"],
    "lang/lisp":            ["racket"],
    "lang/mark":            ["pandoc-bin"],
    "db/postgres":          ["postgresql", "pgadmin4"]

}


plasma = {
    "desktop":                 ["superpaper"],
    "desktop/kvantum":         ["kvantum-qt5-git"],
    "desktop/kvantum/theme":   ["kvantum-theme-layan-git"],
    "desktop/taskbars":        ["plank"],
}

xfce = {
    "xfce":                ["xfce4-settings"],
    "compositor":          ["picom"],
    "applauncher":         ["dmenu", "rofi", "rofi-calc"],
    "desktop":             ["lxappearance", "dunst-git"],

    # -----------------------------------------------------------------------------------#
    #                               Display manager
    # -----------------------------------------------------------------------------------#
    "dm/xorg!":            ["xorg", "xorg-xinit-git"],
    "dm/lightdm":          ["lightdm",
                            "lightdm-gtk-greeter",
                            "lightdm-gtk-greeter-settings",
                            "lightdm-webkit2-greeter"],


    # -----------------------------------------------------------------------------------#
    #                               Themes
    # -----------------------------------------------------------------------------------#
    "themes/icons!":        ["tela-icon-theme-git", "flatery-icon-theme-git"],
    "themes/cursors!":      ["capitaine-cursors"],
    "themes/colors!":       ["ant-dracula-gtk-theme",
                             "chicago95-gtk-theme-git",
                             "gruvbox-material-gtk-theme-git",
                             "yaru-gtk-theme"],


    # -----------------------------------------------------------------------------------#
    #                               i3
    # -----------------------------------------------------------------------------------#
    "i3":                  ["i3-gaps", "autotiling-git", "perl-anyevent-i3"],
    "i3/lock":             ["i3lock"],
    "i3/bar":              ["i3blocks", "py3status", "polybar"],


    # -----------------------------------------------------------------------------------#
    #                               xmonad
    # -----------------------------------------------------------------------------------#
    "xmonad":              ["xmonad", "xmonad-contrib", "xmonad-utils", "xmonad-log"],
    "xmonad/haskell":      ["haskell-dbus"],
    "xmonad/bar":          ["xmobar"]
}
